---
title: Schema.Attribute.Option
framework: SwiftData
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/schema/attribute/option
source_url: 'https://developer.apple.com/documentation/swiftdata/schema/attribute/option'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/schema/attribute/option.json'
content_hash: 'sha256:dfde9e75a1467a15'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftData](../../../swiftdata.md) · [Schema](../../schema.md) · [Attribute](../attribute.md)

# Schema.Attribute.Option

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Option
```

## Relationships

- **Conforms To**: [Copyable](../../../swift/copyable.md), [CustomDebugStringConvertible](../../../swift/customdebugstringconvertible.md), [Decodable](../../../swift/decodable.md), [Encodable](../../../swift/encodable.md), [Equatable](../../../swift/equatable.md), [Escapable](../../../swift/escapable.md), [Hashable](../../../swift/hashable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Accessing property options

- [allowsCloudEncryption](option/allowscloudencryption.md) — Stores the property’s value in an encrypted form.
- [externalStorage](option/externalstorage.md) — Stores the property’s value as binary data adjacent to the model storage.
- [preserveValueOnDeletion](option/preservevalueondeletion.md) — Preserves the property’s value in the persistent history when the context deletes the owning model.
- [spotlight](option/spotlight.md) — Indexes the property’s value so it can appear in Spotlight search results.
- [unique](option/unique.md) — Ensures the property’s value is unique across all models of the same type.
- [transformable(by:)](<option/transformable(by_)-9d4xh.md>) — Transforms the property’s value between an in-memory form and a persisted form.
- [transformable(by:)](<option/transformable(by_)-lunz.md>)
- [ephemeral](option/ephemeral.md) — Track changes to this property but do not persist
- [codable](option/codable.md) — Uses the property’s codable representation to store the property.
