---
title: UTTypeText
framework: Uniform Type Identifiers
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypetext
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypetext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypetext.json'
content_hash: 'sha256:c1e538f5dd23507d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Uniform Type Identifiers](../uniformtypeidentifiers.md)

# UTTypeText

<sub>Global Variable</sub>

A base type that represents all text-encoded data, including text with markup.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern UTType * const UTTypeText;
```

## Discussion

The identifier for this type is `public.text`.

This type conforms to [UTTypeData](uttypedata.md) and [UTTypeContent](uttypecontent.md).

## See Also

### Text files

- [UTTypePlainText](uttypeplaintext.md) — A type that represents text with no markup and an unspecified encoding.
- [UTTypeUTF8PlainText](uttypeutf8plaintext.md) — A type that represents plain text encoded as UTF-8.
- [UTTypeUTF16PlainText](uttypeutf16plaintext.md) — A type that represents plain text encoded as UTF-16 in native byte order with an optional bill of materials.
- [UTTypeUTF16ExternalPlainText](uttypeutf16externalplaintext.md) — A type that represents plain text encoded as UTF-16 with an optional BOM.
- [UTTypeMarkdown](uttypemarkdown.md) — A type that represents Markdown data. _(beta)_
