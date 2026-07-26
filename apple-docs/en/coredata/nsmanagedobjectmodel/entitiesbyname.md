---
title: entitiesByName
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectmodel/entitiesbyname
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/entitiesbyname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectmodel/entitiesbyname.json'
content_hash: 'sha256:f05722cd95ce519d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectModel](../nsmanagedobjectmodel.md)

# entitiesByName

<sub>Instance Property</sub>

The entities of the model, keyed by name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var entitiesByName: [String : NSEntityDescription] { get }
```

## Discussion

Entities are instances of [NSEntityDescription](../nsentitydescription.md).

## See Also

### Related Documentation

- [+ entityForName:inManagedObjectContext:](<../nsentitydescription/entity(forentityname_in_).md>) — Returns the entity with the specified name from the managed object model associated with the specified managed object context’s persistent store coordinator.

### Managing entities and configurations

- [entities](entities.md) — The entities in the model.
- [configurations](configurations.md) — All the available configuration names of the model.
- [- entitiesForConfiguration:](<entities(forconfigurationname_).md>) — Returns the entities of the model for a specified configuration.
- [- setEntities:forConfiguration:](<setentities(__forconfigurationname_).md>) — Associates the specified entities with the model using the given configuration name.
