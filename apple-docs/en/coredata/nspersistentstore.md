---
title: NSPersistentStore
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstore
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstore'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstore.json'
content_hash: 'sha256:1ae683cd5fe48182'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentStore

<sub>Class</sub>

The abstract base class for all Core Data persistent stores.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSPersistentStore
```

## Overview

Core Data provides four store types—SQLite, Binary, XML, and In-Memory (the XML store is not available on iOS); these are described in Persistent Store Features. Core Data also provides subclasses of `NSPersistentStore` that you can use to define your own store types: [NSAtomicStore](nsatomicstore.md) and [NSIncrementalStore](nsincrementalstore.md). The Binary and XML stores are examples of atomic stores that inherit functionality from `NSAtomicStore`.

### Subclassing Notes

You should not subclass `NSPersistentStore` directly. Core Data only supports subclassing of [NSAtomicStore](nsatomicstore.md) and [NSIncrementalStore](nsincrementalstore.md).

The designated initializer is [- initWithPersistentStoreCoordinator:configurationName:URL:options:](<nspersistentstore/init(persistentstorecoordinator_configurationname_at_options_).md>). When you implement the initializer, you must ensure you load metadata during initialization and set it using [metadata](nspersistentstore/metadata.md).

You must override these methods:

- [type](nspersistentstore/type.md)
- [metadata](nspersistentstore/metadata.md)
- [+ metadataForPersistentStoreWithURL:error:](<nspersistentstore/metadataforpersistentstore(with_).md>)
- [+ setMetadata:forPersistentStoreWithURL:error:](<nspersistentstore/setmetadata(__forpersistentstoreat_).md>)

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSAtomicStore](nsatomicstore.md), [NSIncrementalStore](nsincrementalstore.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a Persistent Store

- [- initWithPersistentStoreCoordinator:configurationName:URL:options:](<nspersistentstore/init(persistentstorecoordinator_configurationname_at_options_).md>) — Returns a store initialized with the given arguments.

### Getting Store Configuration

- [configurationName](nspersistentstore/configurationname.md) — The name of the managed object model configuration that creates the persistent store.
- [options](nspersistentstore/options.md) — The options that Core Data uses to create the store.
- [persistentStoreCoordinator](nspersistentstore/persistentstorecoordinator.md) — The persistent store coordinator that loads the persistent store.
- [type](nspersistentstore/type.md) — The type string of the persistent store.
- [StoreType](nspersistentstore/storetype.md) — The types of persistent stores that Core Data supports.
- [Persistent Store Types](persistent-store-types.md) — Persist data through the available store types.

### Managing Store Attributes

- [identifier](nspersistentstore/identifier.md) — The unique identifier for the persistent store.
- [readOnly](nspersistentstore/isreadonly.md) — A Boolean value that indicates whether the persistent store is read-only.
- [URL](nspersistentstore/url.md) — The URL for the persistent store.

### Managing Store Metadata

- [+ metadataForPersistentStoreWithURL:error:](<nspersistentstore/metadataforpersistentstore(with_).md>) — Returns the metadata from the persistent store at the given URL.
- [+ setMetadata:forPersistentStoreWithURL:error:](<nspersistentstore/setmetadata(__forpersistentstoreat_).md>) — Sets the metadata for the store at a given URL.
- [- loadMetadata:](<nspersistentstore/loadmetadata().md>) — Instructs the persistent store to load its metadata.
- [metadata](nspersistentstore/metadata.md) — The metadata for the persistent store.

### Responding to the Store Life Cycle

- [- didAddToPersistentStoreCoordinator:](<nspersistentstore/didadd(to_).md>) — Invoked after the persistent store has been added to the persistent store coordinator.
- [- willRemoveFromPersistentStoreCoordinator:](<nspersistentstore/willremove(from_).md>) — Invoked before the persistent store is removed from the persistent store coordinator.

### Integrating with Spotlight

- [coreSpotlightExporter](nspersistentstore/corespotlightexporter.md) — The spotlight exporter associated with this persistent store.

### Providing a Migration Manager

- [+ migrationManagerClass](<nspersistentstore/migrationmanagerclass().md>) — Returns the migration manager class for this store class.

### Initializers

- [init(persistentStoreCoordinator:configurationName:URL:options:)](<nspersistentstore/init(persistentstorecoordinator_configurationname_url_options_).md>)

## See Also

### Store Coordination

- [NSPersistentStoreCoordinator](nspersistentstorecoordinator.md) — An object that enables an app’s contexts and the underlying persistent stores to work together.
- [NSPersistentStoreDescription](nspersistentstoredescription.md) — A description object used to create and load a persistent store.
- [NSPersistentStoreRequest](nspersistentstorerequest.md) — Criteria used to retrieve data from or save data to a persistent store.
- [NSPersistentStoreResult](nspersistentstoreresult.md) — The abstract base class for results returned from a persistent store coordinator.
- [NSPersistentStoreAsynchronousResult](nspersistentstoreasynchronousresult.md) — A concrete class used to represent the results of an asynchronous request.
- [NSSaveChangesRequest](nssavechangesrequest.md) — An encapsulation of a collection of changes to be made by an object store in response to a save operation on a managed object context.
- [NSAtomicStore](nsatomicstore.md) — An abstract superclass that you subclass to create a Core Data atomic store.
- [NSAtomicStoreCacheNode](nsatomicstorecachenode.md) — A concrete class that you use to represent basic nodes in a Core Data atomic store.
- [NSIncrementalStore](nsincrementalstore.md) — An abstract superclass defining the API through which Core Data communicates with a store.
- [NSIncrementalStoreNode](nsincrementalstorenode.md) — A concrete class used to represent basic nodes in a Core Data incremental store.
