---
title: 'managedObjectContextDidRegisterObjects(with:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsincrementalstore/managedobjectcontextdidregisterobjects(with:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsincrementalstore/managedobjectcontextdidregisterobjects(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsincrementalstore/managedobjectcontextdidregisterobjects%28with%3A%29.json'
content_hash: 'sha256:b189faa43aabe0f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSIncrementalStore](../nsincrementalstore.md)

# managedObjectContextDidRegisterObjects(with:)

<sub>Instance Method</sub>

Indicates that objects identified by a given array of object IDs are in use in a managed object context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func managedObjectContextDidRegisterObjects(with objectIDs: [NSManagedObjectID])
```

## Parameters

- `objectIDs` — An array of object IDs.

## Discussion

This method and [- managedObjectContextDidUnregisterObjectsWithIDs:](<managedobjectcontextdidunregisterobjects(with_).md>) allow managed object contexts to communicate interest in the row data of specific objects in a manner akin to reference counting. For more details, see [- managedObjectContextDidUnregisterObjectsWithIDs:](<managedobjectcontextdidunregisterobjects(with_).md>).

## See Also

### Responding to Context Changes

- [- managedObjectContextDidUnregisterObjectsWithIDs:](<managedobjectcontextdidunregisterobjects(with_).md>) — Indicates that objects identified by a given array of object IDs are no longer being used by a managed object context.
