---
title: UTTypeMarkdown
framework: Uniform Type Identifiers
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [occ]
beta: true
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypemarkdown
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypemarkdown'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypemarkdown.json'
content_hash: 'sha256:15a34f2d76d4b9f8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Uniform Type Identifiers](../uniformtypeidentifiers.md)

# UTTypeMarkdown

<sub>Global Variable</sub>

A type that represents Markdown data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern UTType * const UTTypeMarkdown;
```

## Discussion

The identifier for this type is `net.daringfireball.markdown`.

This type conforms to [UTTypeUTF8PlainText](uttypeutf8plaintext.md).

## See Also

### Text files

- [UTTypeText](uttypetext.md) — A base type that represents all text-encoded data, including text with markup.
- [UTTypePlainText](uttypeplaintext.md) — A type that represents text with no markup and an unspecified encoding.
- [UTTypeUTF8PlainText](uttypeutf8plaintext.md) — A type that represents plain text encoded as UTF-8.
- [UTTypeUTF16PlainText](uttypeutf16plaintext.md) — A type that represents plain text encoded as UTF-16 in native byte order with an optional bill of materials.
- [UTTypeUTF16ExternalPlainText](uttypeutf16externalplaintext.md) — A type that represents plain text encoded as UTF-16 with an optional BOM.
