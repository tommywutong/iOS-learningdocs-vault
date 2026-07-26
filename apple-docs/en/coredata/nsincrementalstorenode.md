---
title: NSIncrementalStoreNode
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsincrementalstorenode
source_url: 'https://developer.apple.com/documentation/coredata/nsincrementalstorenode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsincrementalstorenode.json'
content_hash: 'sha256:42f93873880eb056'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSIncrementalStoreNode

<sub>Class</sub>

A concrete class used to represent basic nodes in a Core Data incremental store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSIncrementalStoreNode
```

## Overview

A node represents a single record in a persistent store.

You can subclass `NSIncrementalStoreNode` to provide custom behavior.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializing a Node

- [- initWithObjectID:withValues:version:](<nsincrementalstorenode/init(objectid_withvalues_version_).md>) — Returns an object initialized with the given values.

### Managing Node Data

- [objectID](nsincrementalstorenode/objectid.md) — The object ID that identifies the data stored by the receiver.
- [- updateWithValues:version:](<nsincrementalstorenode/update(withvalues_version_).md>) — Update the values and version to reflect new data being saved to or loaded from the external store.
- [- valueForPropertyDescription:](<nsincrementalstorenode/value(for_).md>) — Returns the value for the given property.
- [version](nsincrementalstorenode/version.md) — The version of data in the receiver.

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
- [NSAtomicStoreCacheNode](nsatomicstorecachenode.md) — A concrete class that you use to represent basic nodes in a Core Data atomic store.
- [NSIncrementalStore](nsincrementalstore.md) — An abstract superclass defining the API through which Core Data communicates with a store.
