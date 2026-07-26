---
title: shouldDeleteInaccessibleFaults
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontext/shoulddeleteinaccessiblefaults
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/shoulddeleteinaccessiblefaults'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/shoulddeleteinaccessiblefaults.json'
content_hash: 'sha256:6844a404584a4250'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# shouldDeleteInaccessibleFaults

<sub>Instance Property</sub>

A Boolean value that determines whether the context turns inaccessible faults into deleted objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var shouldDeleteInaccessibleFaults: Bool { get set }
```

## Discussion

Use this property to control how the context behaves when it encounters an _inaccessible fault_ — an object with no underlying data in the persistent store. For example, you might fetch an object that has a to-many relationship, but then a background context deletes the related objects from the store before you traverse that relationship.

When this property is set to [true](../../swift/true.md), the context returns a managed object with the following characteristics:

- The object’s attributes, including scalars, nullable, and mandatory attributes are all set to `nil` or `0`.
- The object’s [deleted](../nsmanagedobject/isdeleted.md) property is set to [true](../../swift/true.md), which adds the object to the context’s [deletedObjects](deletedobjects.md) set.
- The object is exempt from validation rules, including optionality, because the object is nonexistent and the context discards it when you next call [- save:](<save().md>) or [- reset](<reset().md>).

When the context returns an object with these characteristics, your app can continue running and process this object in the same way as any other deleted object.

When this property is set to [false](../../swift/false.md), the context throws an exception.

The default value is [true](../../swift/true.md).

> [!note] Note
> You can use query generations to pin a context to a stable view of the store’s data and isolate that context from changes that other contexts or processes make. For more information, see [Accessing data when the store changes](../accessing-data-when-the-store-changes.md).

## See Also

### Handling managed objects

- [insertedObjects](insertedobjects.md) — The set of objects that have been inserted into the context but not yet saved in a persistent store.
- [updatedObjects](updatedobjects.md) — The set of objects registered with the context that have uncommitted changes.
- [deletedObjects](deletedobjects.md) — The set of objects that will be removed from their persistent store during the next save operation.
- [- shouldHandleInaccessibleFault:forObjectID:triggeredByProperty:](<shouldhandleinaccessiblefault(__for_triggeredbyproperty_).md>) — Creates a log of the inaccessible fault.
- [- insertObject:](<insert(__).md>) — Registers an object to be inserted in the context’s persistent store the next time changes are saved.
- [- deleteObject:](<delete(__).md>) — Specifies an object that should be removed from its persistent store when changes are committed.
- [- assignObject:toPersistentStore:](<assign(__to_).md>) — Specifies the store in which a newly inserted object will be saved.
- [- obtainPermanentIDsForObjects:error:](<obtainpermanentids(for_).md>) — Converts to permanent IDs the object IDs of the objects in a given array.
- [- detectConflictsForObject:](<detectconflicts(for_).md>) — Marks an object for conflict detection.
- [- refreshObject:mergeChanges:](<refresh(__mergechanges_).md>) — Updates the persistent properties of a managed object to use the latest values from the persistent store.
- [- processPendingChanges](<processpendingchanges().md>) — Forces the context to process changes to the object graph.
- [- observeValueForKeyPath:ofObject:change:context:](<observevalue(forkeypath_of_change_context_).md>) — Allows a context that has registered as an observer of a value to be notified of a change to that value.
