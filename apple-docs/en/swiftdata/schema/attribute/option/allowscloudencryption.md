---
title: allowsCloudEncryption
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/schema/attribute/option/allowscloudencryption
source_url: 'https://developer.apple.com/documentation/swiftdata/schema/attribute/option/allowscloudencryption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/schema/attribute/option/allowscloudencryption.json'
content_hash: 'sha256:3d22df90f90fc52e'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [SwiftData](../../../../swiftdata.md) · [Schema](../../../schema.md) · [Attribute](../../attribute.md) · [Option](../option.md)

# allowsCloudEncryption

<sub>Type Property</sub>

Stores the property’s value in an encrypted form.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var allowsCloudEncryption: Schema.Attribute.Option { get }
```

## See Also

### Accessing property options

- [externalStorage](externalstorage.md) — Stores the property’s value as binary data adjacent to the model storage.
- [preserveValueOnDeletion](preservevalueondeletion.md) — Preserves the property’s value in the persistent history when the context deletes the owning model.
- [spotlight](spotlight.md) — Indexes the property’s value so it can appear in Spotlight search results.
- [unique](unique.md) — Ensures the property’s value is unique across all models of the same type.
- [transformable(by:)](<transformable(by_)-9d4xh.md>) — Transforms the property’s value between an in-memory form and a persisted form.
- [transformable(by:)](<transformable(by_)-lunz.md>)
- [ephemeral](ephemeral.md) — Track changes to this property but do not persist
- [codable](codable.md) — Uses the property’s codable representation to store the property.
