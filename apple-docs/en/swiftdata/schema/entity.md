---
title: Schema.Entity
framework: SwiftData
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/schema/entity
source_url: 'https://developer.apple.com/documentation/swiftdata/schema/entity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/schema/entity.json'
content_hash: 'sha256:2bf66a002dfc4104'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [Schema](../schema.md)

# Schema.Entity

<sub>Class</sub>

An object that provides a blueprint for the associated model class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class Entity
```

## Relationships

- **Conforms To**: [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating an entity

- [init(_:)](<entity/init(__).md>)
- [init(_:properties:)](<entity/init(__properties_).md>)
- [init(_:subentities:properties:)](<entity/init(__subentities_properties_).md>)

### Assigning identity

- [name](entity/name.md)

### Managing attributes

- [attributes](entity/attributes.md)
- [attributesByName](entity/attributesbyname.md)

### Defining relationships

- [relationships](entity/relationships.md)
- [relationshipsByName](entity/relationshipsbyname.md)

### Managing properties

- [properties](entity/properties.md)
- [inheritedProperties](entity/inheritedproperties.md)
- [inheritedPropertiesByName](entity/inheritedpropertiesbyname.md)
- [storedProperties](entity/storedproperties.md)
- [storedPropertiesByName](entity/storedpropertiesbyname.md)

### Applying constraints

- [uniquenessConstraints](entity/uniquenessconstraints.md)

### Configuring the inheritance chain

- [superentity](entity/superentity.md)
- [superentityName](entity/superentityname.md)
- [subentities](entity/subentities.md)

### Instance Properties

- [indices](entity/indices.md)

## See Also

### Accessing entities

- [entities](entities.md)
- [entitiesByName](entitiesbyname.md)
