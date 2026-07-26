---
title: utf16ExternalPlainText
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttype-swift.struct/utf16externalplaintext
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/utf16externalplaintext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/utf16externalplaintext.json'
content_hash: 'sha256:0a16179a170d131a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# utf16ExternalPlainText

<sub>Type Property</sub>

A type that represents plain text encoded as UTF-16 with an optional bill of materials.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var utf16ExternalPlainText: UTType { get }
```

## Discussion

If the bill of materials isn’t present, the encoding uses “external byte order (big-endian),

The identifier for this type is `public.utf16-external-plain-text`.

This type conforms to [UTTypePlainText](../uttypeplaintext.md).

## See Also

### Text files

- [text](text.md) — A base type that represents all text-encoded data, including text with markup.
- [plainText](plaintext.md) — A type that represents text with no markup and an unspecified encoding.
- [utf8PlainText](utf8plaintext.md) — A type that represents plain text encoded as UTF-8.
- [utf16PlainText](utf16plaintext.md) — A type that represents plain text encoded as UTF-16 in native byte order with an optional bill of materials.
- [markdown](markdown.md) — A type that represents Markdown data. _(beta)_
