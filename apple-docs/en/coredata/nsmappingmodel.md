---
title: NSMappingModel
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmappingmodel
source_url: 'https://developer.apple.com/documentation/coredata/nsmappingmodel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmappingmodel.json'
content_hash: 'sha256:63370dbb36cc3c86'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSMappingModel

<sub>Class</sub>

A model instance that specifies how to map a model from a source to a destination managed object model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSMappingModel
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a Mapping

- [+ mappingModelFromBundles:forSourceModel:destinationModel:](<nsmappingmodel/init(from_forsourcemodel_destinationmodel_).md>) — Returns the mapping model that will translate data from the source to the destination model.
- [+ inferredMappingModelForSourceModel:destinationModel:error:](<nsmappingmodel/inferredmappingmodel(forsourcemodel_destinationmodel_).md>) — Returns a newly created mapping model that will migrate data from the source to the destination model.
- [- initWithContentsOfURL:](<nsmappingmodel/init(contentsof_).md>) — Returns a mapping model initialized from a given URL.

### Managing Entity Mappings

- [entityMappings](nsmappingmodel/entitymappings.md) — The entity mappings for the mapping model.
- [entityMappingsByName](nsmappingmodel/entitymappingsbyname.md) — The entity mappings for the mapping model, keyed by name.

### Initializers

- [init(contentsOfURL:)](<nsmappingmodel/init(contentsofurl_).md>)
- [init(fromBundles:forSourceModel:destinationModel:)](<nsmappingmodel/init(frombundles_forsourcemodel_destinationmodel_).md>)

## See Also

### Entity Mapping

- [NSMigrationManager](nsmigrationmanager.md) — A migration manager instance that performs a migration of data from one persistent store to another using a given mapping model.
- [NSEntityMapping](nsentitymapping.md) — A mapping instance that specifies how to map an entity from a source to a destination managed object model.
- [NSEntityMigrationPolicy](nsentitymigrationpolicy.md) — A policy instance that customizes the migration process for an entity mapping.
- [NSEntityMappingType](nsentitymappingtype.md) — The types for mapping an entity between a source model and a destination model.
- [NSPropertyMapping](nspropertymapping.md) — A mapping instance that specifies in a model how to map from a property in a source entity to a property in a destination entity.
