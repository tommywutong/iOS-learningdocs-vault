---
title: Schema.Relationship.DeleteRule.deny
framework: SwiftData
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/schema/relationship/deleterule-swift.enum/deny
source_url: 'https://developer.apple.com/documentation/swiftdata/schema/relationship/deleterule-swift.enum/deny'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/schema/relationship/deleterule-swift.enum/deny.json'
content_hash: 'sha256:cfbd2091e1baf698'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [SwiftData](../../../../swiftdata.md) · [Schema](../../../schema.md) · [Relationship](../../relationship.md) · [DeleteRule](../deleterule-swift.enum.md)

# Schema.Relationship.DeleteRule.deny

<sub>Case</sub>

A rule that prevents the deletion of a model because it contains one or more references to other models.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case deny
```

## See Also

### Accessing delete rules

- [Schema.Relationship.DeleteRule.cascade](cascade.md) — A rule that deletes any related models.
- [Schema.Relationship.DeleteRule.noAction](noaction.md) — A rule that doesn’t make changes to any related models.
- [Schema.Relationship.DeleteRule.nullify](nullify.md) — A rule that nullifies the related model’s reference to the deleted model.
