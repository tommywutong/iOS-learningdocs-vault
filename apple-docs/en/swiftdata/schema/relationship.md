---
title: Schema.Relationship
framework: SwiftData
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/schema/relationship
source_url: 'https://developer.apple.com/documentation/swiftdata/schema/relationship'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/schema/relationship.json'
content_hash: 'sha256:10a91421fb2be040'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [Schema](../schema.md)

# Schema.Relationship

<sub>Class</sub>

An object that describes the configuration and behavior of a relationship between two model classes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class Relationship
```

## Relationships

- **Conforms To**: [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [SchemaProperty](../schemaproperty.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a relationship

- [init(_:deleteRule:minimumModelCount:maximumModelCount:originalName:inverse:hashModifier:)](<relationship/init(__deleterule_minimummodelcount_maximummodelcount_originalname_inverse_hashmodifier_).md>)

### Managing the configuration

- [keypath](relationship/keypath.md)
- [destination](relationship/destination.md)
- [inverseName](relationship/inversename.md)
- [inverseKeyPath](relationship/inversekeypath.md)
- [deleteRule](relationship/deleterule-swift.property.md)
- [DeleteRule](relationship/deleterule-swift.enum.md) — Describes the rule to apply when deleting a model containing references to other models.
- [isToOneRelationship](relationship/istoonerelationship.md)

### Determining behavior

- [options](relationship/options.md)

### Versioning

- [hashModifier](relationship/hashmodifier.md)

### Structures

- [Option](relationship/option.md)

### Instance Properties

- [maximumModelCount](relationship/maximummodelcount.md)
- [minimumModelCount](relationship/minimummodelcount.md)
