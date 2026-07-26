---
title: UTTypeUTF16PlainText
framework: Uniform Type Identifiers
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypeutf16plaintext
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypeutf16plaintext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypeutf16plaintext.json'
content_hash: 'sha256:926b6e341f1d1991'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Uniform Type Identifiers](../uniformtypeidentifiers.md)

# UTTypeUTF16PlainText

<sub>Global Variable</sub>

A type that represents plain text encoded as UTF-16 in native byte order with an optional bill of materials.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern UTType * const UTTypeUTF16PlainText;
```

## Discussion

The identifier for this type is `public.utf16-plain-text`.

This type conforms to [UTTypePlainText](uttypeplaintext.md).

## See Also

### Text files

- [UTTypeText](uttypetext.md) — A base type that represents all text-encoded data, including text with markup.
- [UTTypePlainText](uttypeplaintext.md) — A type that represents text with no markup and an unspecified encoding.
- [UTTypeUTF8PlainText](uttypeutf8plaintext.md) — A type that represents plain text encoded as UTF-8.
- [UTTypeUTF16ExternalPlainText](uttypeutf16externalplaintext.md) — A type that represents plain text encoded as UTF-16 with an optional BOM.
- [UTTypeMarkdown](uttypemarkdown.md) — A type that represents Markdown data. _(beta)_
