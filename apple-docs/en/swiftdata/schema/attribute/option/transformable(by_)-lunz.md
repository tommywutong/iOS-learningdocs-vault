---
title: 'transformable(by:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/schema/attribute/option/transformable(by:)-lunz'
source_url: 'https://developer.apple.com/documentation/swiftdata/schema/attribute/option/transformable(by:)-lunz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/schema/attribute/option/transformable%28by%3A%29-lunz.json'
content_hash: 'sha256:e30b49dbc5730573'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [SwiftData](../../../../swiftdata.md) · [Schema](../../../schema.md) · [Attribute](../../attribute.md) · [Option](../option.md)

# transformable(by:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func transformable(by transformerName: String) -> Schema.Attribute.Option
```

## See Also

### Accessing property options

- [allowsCloudEncryption](allowscloudencryption.md) — Stores the property’s value in an encrypted form.
- [externalStorage](externalstorage.md) — Stores the property’s value as binary data adjacent to the model storage.
- [preserveValueOnDeletion](preservevalueondeletion.md) — Preserves the property’s value in the persistent history when the context deletes the owning model.
- [spotlight](spotlight.md) — Indexes the property’s value so it can appear in Spotlight search results.
- [unique](unique.md) — Ensures the property’s value is unique across all models of the same type.
- [transformable(by:)](<transformable(by_)-9d4xh.md>) — Transforms the property’s value between an in-memory form and a persisted form.
- [ephemeral](ephemeral.md) — Track changes to this property but do not persist
- [codable](codable.md) — Uses the property’s codable representation to store the property.
