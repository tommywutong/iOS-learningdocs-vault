---
title: utf8PlainText
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttype-swift.struct/utf8plaintext
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/utf8plaintext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/utf8plaintext.json'
content_hash: 'sha256:b8c3c03ec60c09ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# utf8PlainText

<sub>Type Property</sub>

A type that represents plain text encoded as UTF-8.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var utf8PlainText: UTType { get }
```

## Discussion

The identifier for this type is `public.utf8-plain-text`.

This type conforms to [UTTypePlainText](../uttypeplaintext.md).

## See Also

### Text files

- [text](text.md) — A base type that represents all text-encoded data, including text with markup.
- [plainText](plaintext.md) — A type that represents text with no markup and an unspecified encoding.
- [utf16PlainText](utf16plaintext.md) — A type that represents plain text encoded as UTF-16 in native byte order with an optional bill of materials.
- [utf16ExternalPlainText](utf16externalplaintext.md) — A type that represents plain text encoded as UTF-16 with an optional bill of materials.
- [markdown](markdown.md) — A type that represents Markdown data. _(beta)_
