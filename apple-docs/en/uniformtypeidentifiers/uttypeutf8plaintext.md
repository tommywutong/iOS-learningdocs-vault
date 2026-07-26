---
title: UTTypeUTF8PlainText
framework: Uniform Type Identifiers
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypeutf8plaintext
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypeutf8plaintext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypeutf8plaintext.json'
content_hash: 'sha256:f1d4f43be4f80ab6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Uniform Type Identifiers](../uniformtypeidentifiers.md)

# UTTypeUTF8PlainText

<sub>Global Variable</sub>

A type that represents plain text encoded as UTF-8.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern UTType * const UTTypeUTF8PlainText;
```

## Discussion

The identifier for this type is `public.utf8-plain-text`.

This type conforms to [UTTypePlainText](uttypeplaintext.md).

## See Also

### Text files

- [UTTypeText](uttypetext.md) — A base type that represents all text-encoded data, including text with markup.
- [UTTypePlainText](uttypeplaintext.md) — A type that represents text with no markup and an unspecified encoding.
- [UTTypeUTF16PlainText](uttypeutf16plaintext.md) — A type that represents plain text encoded as UTF-16 in native byte order with an optional bill of materials.
- [UTTypeUTF16ExternalPlainText](uttypeutf16externalplaintext.md) — A type that represents plain text encoded as UTF-16 with an optional BOM.
- [UTTypeMarkdown](uttypemarkdown.md) — A type that represents Markdown data. _(beta)_
