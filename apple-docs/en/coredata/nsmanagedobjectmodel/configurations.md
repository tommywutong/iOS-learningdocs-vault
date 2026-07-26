---
title: configurations
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectmodel/configurations
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/configurations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectmodel/configurations.json'
content_hash: 'sha256:729a81cb3d1055b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectModel](../nsmanagedobjectmodel.md)

# configurations

<sub>Instance Property</sub>

All the available configuration names of the model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var configurations: [String] { get }
```

## See Also

### Managing entities and configurations

- [entities](entities.md) — The entities in the model.
- [entitiesByName](entitiesbyname.md) — The entities of the model, keyed by name.
- [- entitiesForConfiguration:](<entities(forconfigurationname_).md>) — Returns the entities of the model for a specified configuration.
- [- setEntities:forConfiguration:](<setentities(__forconfigurationname_).md>) — Associates the specified entities with the model using the given configuration name.
