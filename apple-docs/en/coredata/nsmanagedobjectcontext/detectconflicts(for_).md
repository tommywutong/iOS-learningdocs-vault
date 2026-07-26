---
title: 'detectConflicts(for:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobjectcontext/detectconflicts(for:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/detectconflicts(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/detectconflicts%28for%3A%29.json'
content_hash: 'sha256:1d81ad2a4e0c5481'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# detectConflicts(for:)

<sub>Instance Method</sub>

Marks an object for conflict detection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func detectConflicts(for object: NSManagedObject)
```

## Parameters

- `object` — A managed object.

## Discussion

If on the next invocation of [- save:](<save().md>)     `object` has been modified in its persistent store, the save fails. This allows optimistic locking for unchanged objects. Conflict detection is always performed on changed or deleted objects.

## See Also

### Handling managed objects

- [shouldDeleteInaccessibleFaults](shoulddeleteinaccessiblefaults.md) — A Boolean value that determines whether the context turns inaccessible faults into deleted objects.
- [insertedObjects](insertedobjects.md) — The set of objects that have been inserted into the context but not yet saved in a persistent store.
- [updatedObjects](updatedobjects.md) — The set of objects registered with the context that have uncommitted changes.
- [deletedObjects](deletedobjects.md) — The set of objects that will be removed from their persistent store during the next save operation.
- [- shouldHandleInaccessibleFault:forObjectID:triggeredByProperty:](<shouldhandleinaccessiblefault(__for_triggeredbyproperty_).md>) — Creates a log of the inaccessible fault.
- [- insertObject:](<insert(__).md>) — Registers an object to be inserted in the context’s persistent store the next time changes are saved.
- [- deleteObject:](<delete(__).md>) — Specifies an object that should be removed from its persistent store when changes are committed.
- [- assignObject:toPersistentStore:](<assign(__to_).md>) — Specifies the store in which a newly inserted object will be saved.
- [- obtainPermanentIDsForObjects:error:](<obtainpermanentids(for_).md>) — Converts to permanent IDs the object IDs of the objects in a given array.
- [- refreshObject:mergeChanges:](<refresh(__mergechanges_).md>) — Updates the persistent properties of a managed object to use the latest values from the persistent store.
- [- processPendingChanges](<processpendingchanges().md>) — Forces the context to process changes to the object graph.
- [- observeValueForKeyPath:ofObject:change:context:](<observevalue(forkeypath_of_change_context_).md>) — Allows a context that has registered as an observer of a value to be notified of a change to that value.
