---
title: NSPersistentStoreDescription
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstoredescription
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstoredescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstoredescription.json'
content_hash: 'sha256:a88acf8c10edc430'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentStoreDescription

<sub>Class</sub>

A description object used to create and load a persistent store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSPersistentStoreDescription
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a Persistent Store Description

- [- initWithURL:](<nspersistentstoredescription/init(url_)-ko0l.md>) — Initializes the receiver with a URL for the store.

### Configuring a Persistent Store Description

- [URL](nspersistentstoredescription/url.md) — The URL that the store will use for its location.
- [configuration](nspersistentstoredescription/configuration.md) — The name of the configuration used by this store.
- [timeout](nspersistentstoredescription/timeout.md) — The connection timeout for the associated store.
- [type](nspersistentstoredescription/type.md) — The type of store this description represents.
- [readOnly](nspersistentstoredescription/isreadonly.md) — A flag that indicates whether this store will be read-only.
- [shouldAddStoreAsynchronously](nspersistentstoredescription/shouldaddstoreasynchronously.md) — A flag that determines whether the store is added asynchronously.
- [shouldInferMappingModelAutomatically](nspersistentstoredescription/shouldinfermappingmodelautomatically.md) — A flag indicating whether a mapping model should be created automatically.
- [shouldMigrateStoreAutomatically](nspersistentstoredescription/shouldmigratestoreautomatically.md) — A flag indicating whether the associated persistent store should be migrated automatically.
- [- setOption:forKey:](<nspersistentstoredescription/setoption(__forkey_).md>) — Sets an option on the store.
- [- setValue:forPragmaNamed:](<nspersistentstoredescription/setvalue(__forpragmanamed_).md>) — Allows you to set pragmas for the SQLite store.

### Accessing the Configuration Options

- [options](nspersistentstoredescription/options.md) — A dictionary representation of the options set on the associated persistent store.
- [sqlitePragmas](nspersistentstoredescription/sqlitepragmas.md) — The SQLite pragmas set for the associated persistent store. (read-only)

### Syncing to CloudKit

- [cloudKitContainerOptions](nspersistentstoredescription/cloudkitcontaineroptions.md) — Options that customize how this store description aligns with a CloudKit database.

### Initializers

- [init(URL:)](<nspersistentstoredescription/init(url_)-3snc6.md>)
- [init(URL:)](<nspersistentstoredescription/init(url_)-58ysp.md>)

## See Also

### Store Coordination

- [NSPersistentStoreCoordinator](nspersistentstorecoordinator.md) — An object that enables an app’s contexts and the underlying persistent stores to work together.
- [NSPersistentStore](nspersistentstore.md) — The abstract base class for all Core Data persistent stores.
- [NSPersistentStoreRequest](nspersistentstorerequest.md) — Criteria used to retrieve data from or save data to a persistent store.
- [NSPersistentStoreResult](nspersistentstoreresult.md) — The abstract base class for results returned from a persistent store coordinator.
- [NSPersistentStoreAsynchronousResult](nspersistentstoreasynchronousresult.md) — A concrete class used to represent the results of an asynchronous request.
- [NSSaveChangesRequest](nssavechangesrequest.md) — An encapsulation of a collection of changes to be made by an object store in response to a save operation on a managed object context.
- [NSAtomicStore](nsatomicstore.md) — An abstract superclass that you subclass to create a Core Data atomic store.
- [NSAtomicStoreCacheNode](nsatomicstorecachenode.md) — A concrete class that you use to represent basic nodes in a Core Data atomic store.
- [NSIncrementalStore](nsincrementalstore.md) — An abstract superclass defining the API through which Core Data communicates with a store.
- [NSIncrementalStoreNode](nsincrementalstorenode.md) — A concrete class used to represent basic nodes in a Core Data incremental store.
