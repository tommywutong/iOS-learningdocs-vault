---
title: 'setEntities(_:forConfigurationName:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobjectmodel/setentities(_:forconfigurationname:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/setentities(_:forconfigurationname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectmodel/setentities%28_%3Aforconfigurationname%3A%29.json'
content_hash: 'sha256:92602f631ce70452'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectModel](../nsmanagedobjectmodel.md)

# setEntities(_:forConfigurationName:)

<sub>Instance Method</sub>

Associates the specified entities with the model using the given configuration name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setEntities(_ entities: [NSEntityDescription], forConfigurationName configuration: String)
```

## Parameters

- `entities` — An array of instances of `NSEntityDescription`.

- `configuration` — A name for the configuration.

## Discussion

This method raises an exception if the receiver has been used by an object graph manager.

## See Also

### Managing entities and configurations

- [entities](entities.md) — The entities in the model.
- [entitiesByName](entitiesbyname.md) — The entities of the model, keyed by name.
- [configurations](configurations.md) — All the available configuration names of the model.
- [- entitiesForConfiguration:](<entities(forconfigurationname_).md>) — Returns the entities of the model for a specified configuration.
