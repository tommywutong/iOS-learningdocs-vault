---
title: NSIncrementalStore
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsincrementalstore
source_url: 'https://developer.apple.com/documentation/coredata/nsincrementalstore'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsincrementalstore.json'
content_hash: 'sha256:5621f0651ae2bfdc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSIncrementalStore

<sub>Class</sub>

An abstract superclass defining the API through which Core Data communicates with a store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSIncrementalStore
```

## Overview

You use this interface to create persistent stores that load and save data incrementally, allowing for the management of large and/or shared datasets.

### Subclassing Notes

#### Methods to Override

In a subclass of `NSIncrementalStore`, you _must_ override the following methods to provide behavior appropriate for your store:

- [- loadMetadata:](<nsincrementalstore/loadmetadata().md>)
- [- executeRequest:withContext:error:](<nsincrementalstore/execute(__with_).md>)
- [- newValuesForObjectWithID:withContext:error:](<nsincrementalstore/newvaluesforobject(with_with_).md>)
- [- newValueForRelationship:forObjectWithID:withContext:error:](<nsincrementalstore/newvalue(forrelationship_forobjectwith_with_).md>)
- [- obtainPermanentIDsForObjects:error:](<nsincrementalstore/obtainpermanentids(for_).md>)

You can also optionally override the following methods:

- [+ identifierForNewStoreAtURL:](<nsincrementalstore/identifierfornewstore(at_).md>)
- [- managedObjectContextDidRegisterObjectsWithIDs:](<nsincrementalstore/managedobjectcontextdidregisterobjects(with_).md>)
- [- managedObjectContextDidUnregisterObjectsWithIDs:](<nsincrementalstore/managedobjectcontextdidunregisterobjects(with_).md>)

There is no need to override the methods that you must otherwise override for a subclass of [NSPersistentStore](nspersistentstore.md).

#### Methods that Should Not Be Overridden

In a subclass of `NSIncrementalStore`, you should not override the following methods:

- [- newObjectIDForEntity:referenceObject:](<nsincrementalstore/newobjectid(for_referenceobject_).md>)
- [- referenceObjectForObjectID:](<nsincrementalstore/referenceobject(for_).md>)

## Relationships

- **Inherits From**: [NSPersistentStore](nspersistentstore.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Manipulating Managed Objects

- [- executeRequest:withContext:error:](<nsincrementalstore/execute(__with_).md>) — Returns a value as appropriate for the given request, or nil if the request cannot be completed.
- [- newValuesForObjectWithID:withContext:error:](<nsincrementalstore/newvaluesforobject(with_with_).md>) — Returns an incremental store node encapsulating the persistent external values of the object with a given object ID.
- [- newValueForRelationship:forObjectWithID:withContext:error:](<nsincrementalstore/newvalue(forrelationship_forobjectwith_with_).md>) — Returns the relationship for the given relationship of the object with a given object ID.
- [- obtainPermanentIDsForObjects:error:](<nsincrementalstore/obtainpermanentids(for_).md>) — Returns an array containing the object IDs for a given array of newly-inserted objects.
- [- newObjectIDForEntity:referenceObject:](<nsincrementalstore/newobjectid(for_referenceobject_).md>) — Returns a new object ID that uses given data as the key.
- [- referenceObjectForObjectID:](<nsincrementalstore/referenceobject(for_).md>) — Returns the reference data used to construct a given object ID.

### Responding to Context Changes

- [- managedObjectContextDidRegisterObjectsWithIDs:](<nsincrementalstore/managedobjectcontextdidregisterobjects(with_).md>) — Indicates that objects identified by a given array of object IDs are in use in a managed object context.
- [- managedObjectContextDidUnregisterObjectsWithIDs:](<nsincrementalstore/managedobjectcontextdidunregisterobjects(with_).md>) — Indicates that objects identified by a given array of object IDs are no longer being used by a managed object context.

### Accessing Metadata

- [+ identifierForNewStoreAtURL:](<nsincrementalstore/identifierfornewstore(at_).md>) — Returns the identifier for the store at a given URL.
- [- loadMetadata:](<nsincrementalstore/loadmetadata().md>) — Loads the metadata for the store.

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
- [NSIncrementalStoreNode](nsincrementalstorenode.md) — A concrete class used to represent basic nodes in a Core Data incremental store.
