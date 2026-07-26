---
title: 'refresh(_:mergeChanges:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobjectcontext/refresh(_:mergechanges:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/refresh(_:mergechanges:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/refresh%28_%3Amergechanges%3A%29.json'
content_hash: 'sha256:1d5597def1828e06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# refresh(_:mergeChanges:)

<sub>Instance Method</sub>

Updates the persistent properties of a managed object to use the latest values from the persistent store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func refresh(_ object: NSManagedObject, mergeChanges flag: Bool)
```

## Parameters

- `object` — A managed object.

- `flag` — A Boolean value. If `flag` is [false](../../swift/false.md), the context discards pending changes and the managed object becomes a fault. Upon next access, the context reloads the object’s values from the persistent store or last cached state. If `flag` is [true](../../swift/true.md), the context reloads the object’s property values from the store or the cache. Then the context applies local changes over the newly loaded values. Merging the local values into `object` always succeeds, and never results in a merge conflict.

## Discussion

If you call this method before the [stalenessInterval](stalenessinterval.md) expires, the context reloads the data from the cache instead of fetching from the store. If `flag` is [true](../../swift/true.md), this method doesn’t affect any transient properties. If `flag` is [false](../../swift/false.md), the object disposes the value of transient properties.

You typically use this method to ensure data freshness if multiple managed object contexts share a single persistent store. You can use this method to resolve an optimistic locking failure when attempting to save.

Turning `object` into a fault by setting `flag` to [false](../../swift/false.md) breaks strong references to related managed objects. You can use this method to release a portion of your object graph if you want to constrain memory usage.

## See Also

### Related Documentation

- [stalenessInterval](stalenessinterval.md) — The maximum length of time that may have elapsed since the store previously fetched data before fulfilling a fault issues a new fetch.
- [- reset](<reset().md>) — Returns the context to its base state.

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
- [- detectConflictsForObject:](<detectconflicts(for_).md>) — Marks an object for conflict detection.
- [- processPendingChanges](<processpendingchanges().md>) — Forces the context to process changes to the object graph.
- [- observeValueForKeyPath:ofObject:change:context:](<observevalue(forkeypath_of_change_context_).md>) — Allows a context that has registered as an observer of a value to be notified of a change to that value.
