---
title: NSAtomicStore
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsatomicstore
source_url: 'https://developer.apple.com/documentation/coredata/nsatomicstore'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsatomicstore.json'
content_hash: 'sha256:3939573cb79bd3ba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSAtomicStore

<sub>Class</sub>

An abstract superclass that you subclass to create a Core Data atomic store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSAtomicStore
```

## Overview

Use an atomic store to handle data sets that can be expressed in memory. The atomic store API favors simplicity over performance.

This class provides default implementations of some utility methods. Create a custom atomic store subclass when you have a custom file format that you want to integrate with a Core Data app. When you create a subclass, override the following [NSAtomicStore](nsatomicstore.md) methods:

- [- load:](<nsatomicstore/load().md>)
- [- newCacheNodeForManagedObject:](<nsatomicstore/newcachenode(for_).md>)
- [- newReferenceObjectForManagedObject:](<nsatomicstore/newreferenceobject(for_).md>)
- [- save:](<nsatomicstore/save().md>)
- [- updateCacheNode:fromManagedObject:](<nsatomicstore/updatecachenode(__from_).md>)

Also override the following properties and methods of [NSPersistentStore](nspersistentstore.md), from which the atomic store class inherits:

- [type](nspersistentstore/type.md)
- [identifier](nspersistentstore/identifier.md)
- [metadata](nspersistentstore/metadata.md)
- [+ metadataForPersistentStoreWithURL:error:](<nspersistentstore/metadataforpersistentstore(with_).md>)
- [+ setMetadata:forPersistentStoreWithURL:error:](<nspersistentstore/setmetadata(__forpersistentstoreat_).md>)

`NSAtomicStore` provides a default dictionary of metadata. This dictionary contains the store type and identifier ([NSStoreTypeKey](nsstoretypekey.md) and [NSStoreUUIDKey](nsstoreuuidkey.md)) as well as store versioning information. Subclasses must ensure that the metadata is saved along with the store data.

## Relationships

- **Inherits From**: [NSPersistentStore](nspersistentstore.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializing a Store

- [- initWithPersistentStoreCoordinator:configurationName:URL:options:](<nsatomicstore/init(persistentstorecoordinator_configurationname_at_options_).md>) — Creates an atomic store at the specified location.

### Loading a Store

- [- load:](<nsatomicstore/load().md>) — Loads the cache nodes for the receiver.
- [- objectIDForEntity:referenceObject:](<nsatomicstore/objectid(for_withreferenceobject_).md>) — Returns a managed object ID from the reference data for a specified entity.
- [- addCacheNodes:](<nsatomicstore/addcachenodes(__).md>) — Registers a set of cache nodes with the receiver.

### Updating Cache Nodes

- [- newCacheNodeForManagedObject:](<nsatomicstore/newcachenode(for_).md>) — Returns a new cache node for a given managed object.
- [- newReferenceObjectForManagedObject:](<nsatomicstore/newreferenceobject(for_).md>) — Returns a new reference object for a given managed object.
- [- updateCacheNode:fromManagedObject:](<nsatomicstore/updatecachenode(__from_).md>) — Updates the given cache node using the values in a given managed object.
- [- willRemoveCacheNodes:](<nsatomicstore/willremovecachenodes(__).md>) — Method invoked before the store removes the given collection of cache nodes.

### Saving a Store

- [- save:](<nsatomicstore/save().md>) — Saves the cache nodes.

### Utility Methods

- [- cacheNodes](<nsatomicstore/cachenodes().md>) — Returns the set of cache nodes registered with the receiver.
- [- cacheNodeForObjectID:](<nsatomicstore/cachenode(for_).md>) — Returns the cache node for a given managed object ID.
- [- referenceObjectForObjectID:](<nsatomicstore/referenceobject(for_).md>) — Returns the reference object for a given managed object ID.

## See Also

### Store Coordination

- [NSPersistentStoreCoordinator](nspersistentstorecoordinator.md) — An object that enables an app’s contexts and the underlying persistent stores to work together.
- [NSPersistentStore](nspersistentstore.md) — The abstract base class for all Core Data persistent stores.
- [NSPersistentStoreDescription](nspersistentstoredescription.md) — A description object used to create and load a persistent store.
- [NSPersistentStoreRequest](nspersistentstorerequest.md) — Criteria used to retrieve data from or save data to a persistent store.
- [NSPersistentStoreResult](nspersistentstoreresult.md) — The abstract base class for results returned from a persistent store coordinator.
- [NSPersistentStoreAsynchronousResult](nspersistentstoreasynchronousresult.md) — A concrete class used to represent the results of an asynchronous request.
- [NSSaveChangesRequest](nssavechangesrequest.md) — An encapsulation of a collection of changes to be made by an object store in response to a save operation on a managed object context.
- [NSAtomicStoreCacheNode](nsatomicstorecachenode.md) — A concrete class that you use to represent basic nodes in a Core Data atomic store.
- [NSIncrementalStore](nsincrementalstore.md) — An abstract superclass defining the API through which Core Data communicates with a store.
- [NSIncrementalStoreNode](nsincrementalstorenode.md) — A concrete class used to represent basic nodes in a Core Data incremental store.
