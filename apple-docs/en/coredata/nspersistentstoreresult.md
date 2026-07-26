---
title: NSPersistentStoreResult
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstoreresult
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstoreresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstoreresult.json'
content_hash: 'sha256:219aa97c5dfc8afb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentStoreResult

<sub>Class</sub>

The abstract base class for results returned from a persistent store coordinator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSPersistentStoreResult
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSBatchDeleteResult](nsbatchdeleteresult.md), [NSBatchInsertResult](nsbatchinsertresult.md), [NSBatchUpdateResult](nsbatchupdateresult.md), [NSPersistentCloudKitContainerEventResult](nspersistentcloudkitcontainereventresult.md), [NSPersistentHistoryResult](nspersistenthistoryresult.md), [NSPersistentStoreAsynchronousResult](nspersistentstoreasynchronousresult.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

### Store Coordination

- [NSPersistentStoreCoordinator](nspersistentstorecoordinator.md) — An object that enables an app’s contexts and the underlying persistent stores to work together.
- [NSPersistentStore](nspersistentstore.md) — The abstract base class for all Core Data persistent stores.
- [NSPersistentStoreDescription](nspersistentstoredescription.md) — A description object used to create and load a persistent store.
- [NSPersistentStoreRequest](nspersistentstorerequest.md) — Criteria used to retrieve data from or save data to a persistent store.
- [NSPersistentStoreAsynchronousResult](nspersistentstoreasynchronousresult.md) — A concrete class used to represent the results of an asynchronous request.
- [NSSaveChangesRequest](nssavechangesrequest.md) — An encapsulation of a collection of changes to be made by an object store in response to a save operation on a managed object context.
- [NSAtomicStore](nsatomicstore.md) — An abstract superclass that you subclass to create a Core Data atomic store.
- [NSAtomicStoreCacheNode](nsatomicstorecachenode.md) — A concrete class that you use to represent basic nodes in a Core Data atomic store.
- [NSIncrementalStore](nsincrementalstore.md) — An abstract superclass defining the API through which Core Data communicates with a store.
- [NSIncrementalStoreNode](nsincrementalstorenode.md) — A concrete class used to represent basic nodes in a Core Data incremental store.
