---
title: NSPropertyMapping
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspropertymapping
source_url: 'https://developer.apple.com/documentation/coredata/nspropertymapping'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspropertymapping.json'
content_hash: 'sha256:d51a9cf69d5a0b91'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPropertyMapping

<sub>Class</sub>

A mapping instance that specifies in a model how to map from a property in a source entity to a property in a destination entity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSPropertyMapping
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Managing Mapping Attributes

- [name](nspropertymapping/name.md) — The name of the property in the destination entity for the property mapping.
- [valueExpression](nspropertymapping/valueexpression.md) — The value expression for the property mapping.
- [userInfo](nspropertymapping/userinfo.md) — The user info for the property mapping.

## See Also

### Entity Mapping

- [NSMigrationManager](nsmigrationmanager.md) — A migration manager instance that performs a migration of data from one persistent store to another using a given mapping model.
- [NSMappingModel](nsmappingmodel.md) — A model instance that specifies how to map a model from a source to a destination managed object model.
- [NSEntityMapping](nsentitymapping.md) — A mapping instance that specifies how to map an entity from a source to a destination managed object model.
- [NSEntityMigrationPolicy](nsentitymigrationpolicy.md) — A policy instance that customizes the migration process for an entity mapping.
- [NSEntityMappingType](nsentitymappingtype.md) — The types for mapping an entity between a source model and a destination model.
