---
title: NSEntityMappingType
framework: Core Data
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitymappingtype
source_url: 'https://developer.apple.com/documentation/coredata/nsentitymappingtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitymappingtype.json'
content_hash: 'sha256:484f68a635127d40'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSEntityMappingType

<sub>Enumeration</sub>

The types for mapping an entity between a source model and a destination model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NSEntityMappingType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [NSAddEntityMappingType](nsentitymappingtype/addentitymappingtype.md) — Specifies that this is a new entity in the destination model.
- [NSCopyEntityMappingType](nsentitymappingtype/copyentitymappingtype.md) — Specifies that source instances are migrated as-is.
- [NSCustomEntityMappingType](nsentitymappingtype/customentitymappingtype.md) — Specifies a custom mapping.
- [NSRemoveEntityMappingType](nsentitymappingtype/removeentitymappingtype.md) — Specifies that this entity is not present in the destination model.
- [NSTransformEntityMappingType](nsentitymappingtype/transformentitymappingtype.md) — Specifies that entity exists in source and destination and is mapped.
- [NSUndefinedEntityMappingType](nsentitymappingtype/undefinedentitymappingtype.md) — Specifies that the developer handles destination instance creation.

### Initializers

- [init(rawValue:)](<nsentitymappingtype/init(rawvalue_).md>)

## See Also

### Entity Mapping

- [NSMigrationManager](nsmigrationmanager.md) — A migration manager instance that performs a migration of data from one persistent store to another using a given mapping model.
- [NSMappingModel](nsmappingmodel.md) — A model instance that specifies how to map a model from a source to a destination managed object model.
- [NSEntityMapping](nsentitymapping.md) — A mapping instance that specifies how to map an entity from a source to a destination managed object model.
- [NSEntityMigrationPolicy](nsentitymigrationpolicy.md) — A policy instance that customizes the migration process for an entity mapping.
- [NSPropertyMapping](nspropertymapping.md) — A mapping instance that specifies in a model how to map from a property in a source entity to a property in a destination entity.
