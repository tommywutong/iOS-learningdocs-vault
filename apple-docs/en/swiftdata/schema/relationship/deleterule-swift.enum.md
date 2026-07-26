---
title: Schema.Relationship.DeleteRule
framework: SwiftData
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/schema/relationship/deleterule-swift.enum
source_url: 'https://developer.apple.com/documentation/swiftdata/schema/relationship/deleterule-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/schema/relationship/deleterule-swift.enum.json'
content_hash: 'sha256:8efdafd26e3331ec'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftData](../../../swiftdata.md) · [Schema](../../schema.md) · [Relationship](../relationship.md)

# Schema.Relationship.DeleteRule

<sub>Enumeration</sub>

Describes the rule to apply when deleting a model containing references to other models.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum DeleteRule
```

## Relationships

- **Conforms To**: [Copyable](../../../swift/copyable.md), [Decodable](../../../swift/decodable.md), [Encodable](../../../swift/encodable.md), [Equatable](../../../swift/equatable.md), [Escapable](../../../swift/escapable.md), [Hashable](../../../swift/hashable.md), [RawRepresentable](../../../swift/rawrepresentable.md)

## Topics

### Accessing delete rules

- [Schema.Relationship.DeleteRule.cascade](deleterule-swift.enum/cascade.md) — A rule that deletes any related models.
- [Schema.Relationship.DeleteRule.deny](deleterule-swift.enum/deny.md) — A rule that prevents the deletion of a model because it contains one or more references to other models.
- [Schema.Relationship.DeleteRule.noAction](deleterule-swift.enum/noaction.md) — A rule that doesn’t make changes to any related models.
- [Schema.Relationship.DeleteRule.nullify](deleterule-swift.enum/nullify.md) — A rule that nullifies the related model’s reference to the deleted model.

## See Also

### Managing the configuration

- [keypath](keypath.md)
- [destination](destination.md)
- [inverseName](inversename.md)
- [inverseKeyPath](inversekeypath.md)
- [deleteRule](deleterule-swift.property.md)
- [isToOneRelationship](istoonerelationship.md)
