---
title: Schema.Relationship.DeleteRule.noAction
framework: SwiftData
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/schema/relationship/deleterule-swift.enum/noaction
source_url: 'https://developer.apple.com/documentation/swiftdata/schema/relationship/deleterule-swift.enum/noaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/schema/relationship/deleterule-swift.enum/noaction.json'
content_hash: 'sha256:472afd2d22de7390'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [SwiftData](../../../../swiftdata.md) · [Schema](../../../schema.md) · [Relationship](../../relationship.md) · [DeleteRule](../deleterule-swift.enum.md)

# Schema.Relationship.DeleteRule.noAction

<sub>Case</sub>

A rule that doesn’t make changes to any related models.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case noAction
```

## Discussion

Ensure that you take the appropriate action on any related models when using this delete rule, such as deleting them or nullifying their references to the deleted model. Otherwise, your data will be in an inconsistent state and may reference models that don’t exist.

## See Also

### Accessing delete rules

- [Schema.Relationship.DeleteRule.cascade](cascade.md) — A rule that deletes any related models.
- [Schema.Relationship.DeleteRule.deny](deny.md) — A rule that prevents the deletion of a model because it contains one or more references to other models.
- [Schema.Relationship.DeleteRule.nullify](nullify.md) — A rule that nullifies the related model’s reference to the deleted model.
