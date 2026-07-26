---
title: entities
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectmodel/entities
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/entities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectmodel/entities.json'
content_hash: 'sha256:2dfbae36962fe5f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectModel](../nsmanagedobjectmodel.md)

# entities

<sub>Instance Property</sub>

The entities in the model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var entities: [NSEntityDescription] { get set }
```

## Discussion

Entities are instances of [NSEntityDescription](../nsentitydescription.md).

### Special Considerations

Setting the entities for an object model raises an exception if the object model has been used by an object graph manager.

## See Also

### Managing entities and configurations

- [entitiesByName](entitiesbyname.md) — The entities of the model, keyed by name.
- [configurations](configurations.md) — All the available configuration names of the model.
- [- entitiesForConfiguration:](<entities(forconfigurationname_).md>) — Returns the entities of the model for a specified configuration.
- [- setEntities:forConfiguration:](<setentities(__forconfigurationname_).md>) — Associates the specified entities with the model using the given configuration name.
