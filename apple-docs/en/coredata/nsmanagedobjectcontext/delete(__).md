---
title: 'delete(_:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobjectcontext/delete(_:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/delete(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/delete%28_%3A%29.json'
content_hash: 'sha256:8ed1f881c82f72bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# delete(_:)

<sub>Instance Method</sub>

Specifies an object that should be removed from its persistent store when changes are committed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func delete(_ object: NSManagedObject)
```

## Parameters

- `object` — A managed object.

## Discussion

When changes are committed, `object` will be removed from the uniquing tables. If `object` has not yet been saved to a persistent store, it is simply removed from the receiver.

## See Also

### Related Documentation

- [deleted](../nsmanagedobject/isdeleted.md) — A Boolean value that indicates whether the managed object will be deleted during the next save.

### Handling managed objects

- [shouldDeleteInaccessibleFaults](shoulddeleteinaccessiblefaults.md) — A Boolean value that determines whether the context turns inaccessible faults into deleted objects.
- [insertedObjects](insertedobjects.md) — The set of objects that have been inserted into the context but not yet saved in a persistent store.
- [updatedObjects](updatedobjects.md) — The set of objects registered with the context that have uncommitted changes.
- [deletedObjects](deletedobjects.md) — The set of objects that will be removed from their persistent store during the next save operation.
- [- shouldHandleInaccessibleFault:forObjectID:triggeredByProperty:](<shouldhandleinaccessiblefault(__for_triggeredbyproperty_).md>) — Creates a log of the inaccessible fault.
- [- insertObject:](<insert(__).md>) — Registers an object to be inserted in the context’s persistent store the next time changes are saved.
- [- assignObject:toPersistentStore:](<assign(__to_).md>) — Specifies the store in which a newly inserted object will be saved.
- [- obtainPermanentIDsForObjects:error:](<obtainpermanentids(for_).md>) — Converts to permanent IDs the object IDs of the objects in a given array.
- [- detectConflictsForObject:](<detectconflicts(for_).md>) — Marks an object for conflict detection.
- [- refreshObject:mergeChanges:](<refresh(__mergechanges_).md>) — Updates the persistent properties of a managed object to use the latest values from the persistent store.
- [- processPendingChanges](<processpendingchanges().md>) — Forces the context to process changes to the object graph.
- [- observeValueForKeyPath:ofObject:change:context:](<observevalue(forkeypath_of_change_context_).md>) — Allows a context that has registered as an observer of a value to be notified of a change to that value.
