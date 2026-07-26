---
title: codable
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/schema/attribute/option/codable
source_url: 'https://developer.apple.com/documentation/swiftdata/schema/attribute/option/codable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/schema/attribute/option/codable.json'
content_hash: 'sha256:84b36720d92777a4'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [SwiftData](../../../../swiftdata.md) · [Schema](../../../schema.md) · [Attribute](../../attribute.md) · [Option](../option.md)

# codable

<sub>Type Property</sub>

Uses the property’s codable representation to store the property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var codable: Schema.Attribute.Option { get }
```

## See Also

### Accessing property options

- [allowsCloudEncryption](allowscloudencryption.md) — Stores the property’s value in an encrypted form.
- [externalStorage](externalstorage.md) — Stores the property’s value as binary data adjacent to the model storage.
- [preserveValueOnDeletion](preservevalueondeletion.md) — Preserves the property’s value in the persistent history when the context deletes the owning model.
- [spotlight](spotlight.md) — Indexes the property’s value so it can appear in Spotlight search results.
- [unique](unique.md) — Ensures the property’s value is unique across all models of the same type.
- [transformable(by:)](<transformable(by_)-9d4xh.md>) — Transforms the property’s value between an in-memory form and a persisted form.
- [transformable(by:)](<transformable(by_)-lunz.md>)
- [ephemeral](ephemeral.md) — Track changes to this property but do not persist
