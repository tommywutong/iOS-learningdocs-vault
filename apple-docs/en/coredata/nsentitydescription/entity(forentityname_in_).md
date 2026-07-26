---
title: 'entity(forEntityName:in:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsentitydescription/entity(forentityname:in:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsentitydescription/entity(forentityname:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitydescription/entity%28forentityname%3Ain%3A%29.json'
content_hash: 'sha256:37e0fe7c5e2b7961'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityDescription](../nsentitydescription.md)

# entity(forEntityName:in:)

<sub>Type Method</sub>

Returns the entity with the specified name from the managed object model associated with the specified managed object context’s persistent store coordinator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func entity(forEntityName entityName: String, in context: NSManagedObjectContext) -> NSEntityDescription?
```

## Parameters

- `entityName` — The name of an entity.

- `context` — The managed object context to use. Must not be `nil`.

## Return Value

The entity with the specified name from the managed object model associated with `context`’s persistent store coordinator.

## Discussion

Raises [internalInconsistencyException](../../foundation/nsexceptionname/internalinconsistencyexception.md) if `context` is `nil`.

This method is functionally equivalent to the following code example.

```objc
NSManagedObjectModel *managedObjectModel = [[context persistentStoreCoordinator] managedObjectModel];
NSEntityDescription *entity = [[managedObjectModel entitiesByName] objectForKey:entityName];
return entity;
```

## See Also

### Related Documentation

- [entitiesByName](../nsmanagedobjectmodel/entitiesbyname.md) — The entities of the model, keyed by name.
