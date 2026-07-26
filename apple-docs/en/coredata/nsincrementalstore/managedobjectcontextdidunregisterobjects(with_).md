---
title: 'managedObjectContextDidUnregisterObjects(with:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsincrementalstore/managedobjectcontextdidunregisterobjects(with:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsincrementalstore/managedobjectcontextdidunregisterobjects(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsincrementalstore/managedobjectcontextdidunregisterobjects%28with%3A%29.json'
content_hash: 'sha256:9ac514faf4a23e40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSIncrementalStore](../nsincrementalstore.md)

# managedObjectContextDidUnregisterObjects(with:)

<sub>Instance Method</sub>

Indicates that objects identified by a given array of object IDs are no longer being used by a managed object context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func managedObjectContextDidUnregisterObjects(with objectIDs: [NSManagedObjectID])
```

## Parameters

- `objectIDs` — An array of object IDs.

## Discussion

This method is the counterpart to [- managedObjectContextDidRegisterObjectsWithIDs:](<managedobjectcontextdidregisterobjects(with_).md>).

Passing an object ID in the object IDs array of [- managedObjectContextDidRegisterObjectsWithIDs:](<managedobjectcontextdidregisterobjects(with_).md>) is akin to incrementing the object ID’s reference count by 1; passing an object ID in the object IDs array of [- managedObjectContextDidUnregisterObjectsWithIDs:](<managedobjectcontextdidunregisterobjects(with_).md>) is akin to decrementing the object ID’s reference count by 1. It is only when an object ID’s reference count is 0 that no contexts indicate that they are using the corresponding managed object. (Object IDs start with a reference count of 0.)

For example, if the register methods is invoked on two occasions when the object IDs array contains a given object ID, and the unregister method is invoked once when the object IDs array contains that object ID, then a context is still using the object with the given ID.

## See Also

### Responding to Context Changes

- [- managedObjectContextDidRegisterObjectsWithIDs:](<managedobjectcontextdidregisterobjects(with_).md>) — Indicates that objects identified by a given array of object IDs are in use in a managed object context.
