---
title: markdown
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttype-swift.struct/markdown
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/markdown'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/markdown.json'
content_hash: 'sha256:b4b72d63912a980a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# markdown

<sub>Type Property</sub>

A type that represents Markdown data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var markdown: UTType { get }
```

## Discussion

The identifier for this type is `net.daringfireball.markdown`.

This type conforms to [utf8PlainText](utf8plaintext.md).

## See Also

### Text files

- [text](text.md) — A base type that represents all text-encoded data, including text with markup.
- [plainText](plaintext.md) — A type that represents text with no markup and an unspecified encoding.
- [utf8PlainText](utf8plaintext.md) — A type that represents plain text encoded as UTF-8.
- [utf16PlainText](utf16plaintext.md) — A type that represents plain text encoded as UTF-16 in native byte order with an optional bill of materials.
- [utf16ExternalPlainText](utf16externalplaintext.md) — A type that represents plain text encoded as UTF-16 with an optional bill of materials.
