---
title: SchemaProperty
framework: SwiftData
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/schemaproperty
source_url: 'https://developer.apple.com/documentation/swiftdata/schemaproperty'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/schemaproperty.json'
content_hash: 'sha256:72fb10e576f0a054'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# SchemaProperty

<sub>Protocol</sub>

An interface for describing a property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol SchemaProperty : Decodable, Encodable, Hashable
```

## Relationships

- **Inherits From**: [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

- **Conforming Types**: [Attribute](schema/attribute.md), [CompositeAttribute](schema/compositeattribute.md), [Index](schema/index.md), [Relationship](schema/relationship.md), [Unique](schema/unique.md)

## Topics

### Instance Properties

- [isAttribute](schemaproperty/isattribute.md)
- [isOptional](schemaproperty/isoptional.md)
- [isRelationship](schemaproperty/isrelationship.md)
- [isTransient](schemaproperty/istransient.md)
- [isUnique](schemaproperty/isunique.md)
- [name](schemaproperty/name.md)
- [originalName](schemaproperty/originalname.md)
- [valueType](schemaproperty/valuetype.md)

## See Also

### Properties

- [RelationshipCollection](relationshipcollection.md) — An interface for describing a collection of related models.
