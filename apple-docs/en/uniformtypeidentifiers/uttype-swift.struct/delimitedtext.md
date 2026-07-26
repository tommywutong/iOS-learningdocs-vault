---
title: delimitedText
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttype-swift.struct/delimitedtext
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/delimitedtext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/delimitedtext.json'
content_hash: 'sha256:1878cd621c719bbc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# delimitedText

<sub>Type Property</sub>

A base type that represents text containing delimited values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var delimitedText: UTType { get }
```

## Discussion

The identifier for this type is `public.delimited-values-text`.

This type conforms to [UTTypeText](../uttypetext.md).

## See Also

### Data interchange formats

- [commaSeparatedText](commaseparatedtext.md) — A type that represents text containing comma-separated values.
- [tabSeparatedText](tabseparatedtext.md) — A type that represents text containing tab-separated values.
- [utf8TabSeparatedText](utf8tabseparatedtext.md) — A type that represents UTF-8–encoded text containing tab-separated values.
- [rtf](rtf.md) — A type that represents Rich Text Format data.
- [xml](xml.md) — A type that represents generic XML data.
- [yaml](yaml.md) — A type that represents Yet Another Markup Language data.
- [json](json.md) — A type that represents JavaScript Object Notation (JSON) data.
- [vCard](vcard.md) — A type that represents a vCard file.
