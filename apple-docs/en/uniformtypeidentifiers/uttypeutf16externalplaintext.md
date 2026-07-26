---
title: UTTypeUTF16ExternalPlainText
framework: Uniform Type Identifiers
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypeutf16externalplaintext
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypeutf16externalplaintext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypeutf16externalplaintext.json'
content_hash: 'sha256:3b68ae08a9db446a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Uniform Type Identifiers](../uniformtypeidentifiers.md)

# UTTypeUTF16ExternalPlainText

<sub>Global Variable</sub>

A type that represents plain text encoded as UTF-16 with an optional BOM.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern UTType * const UTTypeUTF16ExternalPlainText;
```

## Discussion

If the bill of materials isn’t present, the encoding uses “external byte order (big-endian),

The identifier for this type is `public.utf16-external-plain-text`.

This type conforms to [UTTypePlainText](uttypeplaintext.md).

## See Also

### Text files

- [UTTypeText](uttypetext.md) — A base type that represents all text-encoded data, including text with markup.
- [UTTypePlainText](uttypeplaintext.md) — A type that represents text with no markup and an unspecified encoding.
- [UTTypeUTF8PlainText](uttypeutf8plaintext.md) — A type that represents plain text encoded as UTF-8.
- [UTTypeUTF16PlainText](uttypeutf16plaintext.md) — A type that represents plain text encoded as UTF-16 in native byte order with an optional bill of materials.
- [UTTypeMarkdown](uttypemarkdown.md) — A type that represents Markdown data. _(beta)_
