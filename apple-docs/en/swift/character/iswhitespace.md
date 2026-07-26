---
title: isWhitespace
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/character/iswhitespace
source_url: 'https://developer.apple.com/documentation/swift/character/iswhitespace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/character/iswhitespace.json'
content_hash: 'sha256:f0851371880cef16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Character](../character.md)

# isWhitespace

<sub>Instance Property</sub>

A Boolean value indicating whether this character represents whitespace, including newlines.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isWhitespace: Bool { get }
```

## Discussion

For example, the following characters all represent whitespace:

- “\\t” (U+0009 CHARACTER TABULATION)
- “ “ (U+0020 SPACE)
- U+2029 PARAGRAPH SEPARATOR
- U+3000 IDEOGRAPHIC SPACE

## See Also

### Inspecting a Character

- [isLetter](isletter.md) — A Boolean value indicating whether this character is a letter.
- [isPunctuation](ispunctuation.md) — A Boolean value indicating whether this character represents punctuation.
- [isNewline](isnewline.md) — A Boolean value indicating whether this character represents a newline.
- [isSymbol](issymbol.md) — A Boolean value indicating whether this character represents a symbol.
- [isMathSymbol](ismathsymbol.md) — A Boolean value indicating whether this character represents a symbol that naturally appears in mathematical contexts.
- [isCurrencySymbol](iscurrencysymbol.md) — A Boolean value indicating whether this character represents a currency symbol.
