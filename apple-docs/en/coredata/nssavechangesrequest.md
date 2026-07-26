---
title: NSSaveChangesRequest
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nssavechangesrequest
source_url: 'https://developer.apple.com/documentation/coredata/nssavechangesrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nssavechangesrequest.json'
content_hash: 'sha256:eae8885e42d97029'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSSaveChangesRequest

<sub>Class</sub>

An encapsulation of a collection of changes to be made by an object store in response to a save operation on a managed object context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSSaveChangesRequest
```

## Relationships

- **Inherits From**: [NSPersistentStoreRequest](nspersistentstorerequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializing a Request

- [- initWithInsertedObjects:updatedObjects:deletedObjects:lockedObjects:](<nssavechangesrequest/init(inserted_updated_deleted_locked_).md>) — Initializes a save changes request with collections of given changes.

### Getting Information about a Request

- [insertedObjects](nssavechangesrequest/insertedobjects.md) — The objects that were inserted into the calling context.
- [updatedObjects](nssavechangesrequest/updatedobjects.md) — The objects that were modified in the calling context.
- [deletedObjects](nssavechangesrequest/deletedobjects.md) — The objects that were deleted in the calling context.
- [lockedObjects](nssavechangesrequest/lockedobjects.md) — The objects that were flagged for optimistic locking on the calling context.

### Initializers

- [init(insertedObjects:updatedObjects:deletedObjects:lockedObjects:)](<nssavechangesrequest/init(insertedobjects_updatedobjects_deletedobjects_lockedobjects_).md>)

## See Also

### Store Coordination

- [NSPersistentStoreCoordinator](nspersistentstorecoordinator.md) — An object that enables an app’s contexts and the underlying persistent stores to work together.
- [NSPersistentStore](nspersistentstore.md) — The abstract base class for all Core Data persistent stores.
- [NSPersistentStoreDescription](nspersistentstoredescription.md) — A description object used to create and load a persistent store.
- [NSPersistentStoreRequest](nspersistentstorerequest.md) — Criteria used to retrieve data from or save data to a persistent store.
- [NSPersistentStoreResult](nspersistentstoreresult.md) — The abstract base class for results returned from a persistent store coordinator.
- [NSPersistentStoreAsynchronousResult](nspersistentstoreasynchronousresult.md) — A concrete class used to represent the results of an asynchronous request.
- [NSAtomicStore](nsatomicstore.md) — An abstract superclass that you subclass to create a Core Data atomic store.
- [NSAtomicStoreCacheNode](nsatomicstorecachenode.md) — A concrete class that you use to represent basic nodes in a Core Data atomic store.
- [NSIncrementalStore](nsincrementalstore.md) — An abstract superclass defining the API through which Core Data communicates with a store.
- [NSIncrementalStoreNode](nsincrementalstorenode.md) — A concrete class used to represent basic nodes in a Core Data incremental store.
