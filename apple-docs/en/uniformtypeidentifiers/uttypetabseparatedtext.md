---
title: UTTypeTabSeparatedText
framework: Uniform Type Identifiers
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypetabseparatedtext
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypetabseparatedtext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypetabseparatedtext.json'
content_hash: 'sha256:7a0c5c1b1f073162'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Uniform Type Identifiers](../uniformtypeidentifiers.md)

# UTTypeTabSeparatedText

<sub>Global Variable</sub>

A type that represents text containing tab-separated values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern UTType * const UTTypeTabSeparatedText;
```

## Discussion

The identifier for this type is `public.tab-separated-values-text`.

This type conforms to [UTTypeDelimitedText](uttypedelimitedtext.md).

## See Also

### Data interchange formats

- [UTTypeDelimitedText](uttypedelimitedtext.md) — A base type that represents text containing delimited values.
- [UTTypeCommaSeparatedText](uttypecommaseparatedtext.md) — A type that represents text containing comma-separated values.
- [UTTypeUTF8TabSeparatedText](uttypeutf8tabseparatedtext.md) — A type that represents UTF-8–encoded text containing tab-separated values.
- [UTTypeRTF](uttypertf.md) — A type that represents Rich Text Format data.
- [UTTypeXML](uttypexml.md) — A type that represents generic XML data.
- [UTTypeYAML](uttypeyaml.md) — A type that represents Yet Another Markup Language data.
- [UTTypeJSON](uttypejson.md) — A type that represents JavaScript Object Notation (JSON) data.
- [UTTypeVCard](uttypevcard.md) — A type that represents a vCard file.
