---
title: NSAtomicStoreCacheNode
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsatomicstorecachenode
source_url: 'https://developer.apple.com/documentation/coredata/nsatomicstorecachenode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsatomicstorecachenode.json'
content_hash: 'sha256:1d69aa43fc81216c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSAtomicStoreCacheNode

<sub>Class</sub>

A concrete class that you use to represent basic nodes in a Core Data atomic store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSAtomicStoreCacheNode
```

## Overview

A node represents a single record in a persistent store.

You can subclass `NSAtomicStoreCacheNode` to provide custom behavior.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializing a Cache Node

- [- initWithObjectID:](<nsatomicstorecachenode/init(objectid_).md>) — Returns a cache node for the given managed object ID.

### Managing Node Data

- [objectID](nsatomicstorecachenode/objectid.md) — The managed object ID of the node.
- [propertyCache](nsatomicstorecachenode/propertycache.md) — The property cache dictionary of the node.
- [- valueForKey:](<nsatomicstorecachenode/value(forkey_).md>) — Returns the value for a given key.
- [- setValue:forKey:](<nsatomicstorecachenode/setvalue(__forkey_).md>) — Sets the value for the given key.

## See Also

### Store Coordination

- [NSPersistentStoreCoordinator](nspersistentstorecoordinator.md) — An object that enables an app’s contexts and the underlying persistent stores to work together.
- [NSPersistentStore](nspersistentstore.md) — The abstract base class for all Core Data persistent stores.
- [NSPersistentStoreDescription](nspersistentstoredescription.md) — A description object used to create and load a persistent store.
- [NSPersistentStoreRequest](nspersistentstorerequest.md) — Criteria used to retrieve data from or save data to a persistent store.
- [NSPersistentStoreResult](nspersistentstoreresult.md) — The abstract base class for results returned from a persistent store coordinator.
- [NSPersistentStoreAsynchronousResult](nspersistentstoreasynchronousresult.md) — A concrete class used to represent the results of an asynchronous request.
- [NSSaveChangesRequest](nssavechangesrequest.md) — An encapsulation of a collection of changes to be made by an object store in response to a save operation on a managed object context.
- [NSAtomicStore](nsatomicstore.md) — An abstract superclass that you subclass to create a Core Data atomic store.
- [NSIncrementalStore](nsincrementalstore.md) — An abstract superclass defining the API through which Core Data communicates with a store.
- [NSIncrementalStoreNode](nsincrementalstorenode.md) — A concrete class used to represent basic nodes in a Core Data incremental store.
