---
title: 'entities(forConfigurationName:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobjectmodel/entities(forconfigurationname:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/entities(forconfigurationname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectmodel/entities%28forconfigurationname%3A%29.json'
content_hash: 'sha256:107c055c757310c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectModel](../nsmanagedobjectmodel.md)

# entities(forConfigurationName:)

<sub>Instance Method</sub>

Returns the entities of the model for a specified configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func entities(forConfigurationName configuration: String?) -> [NSEntityDescription]?
```

## Parameters

- `configuration` — The name of a configuration in the receiver.

## Return Value

An array containing the entities of the receiver for the configuration specified by `configuration`.

## See Also

### Managing entities and configurations

- [entities](entities.md) — The entities in the model.
- [entitiesByName](entitiesbyname.md) — The entities of the model, keyed by name.
- [configurations](configurations.md) — All the available configuration names of the model.
- [- setEntities:forConfiguration:](<setentities(__forconfigurationname_).md>) — Associates the specified entities with the model using the given configuration name.
