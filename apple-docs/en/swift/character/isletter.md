---
title: isLetter
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/character/isletter
source_url: 'https://developer.apple.com/documentation/swift/character/isletter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/character/isletter.json'
content_hash: 'sha256:5838ffb936596334'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Character](../character.md)

# isLetter

<sub>Instance Property</sub>

A Boolean value indicating whether this character is a letter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isLetter: Bool { get }
```

## Discussion

For example, the following characters are all letters:

- “A” (U+0041 LATIN CAPITAL LETTER A)
- “é” (U+0065 LATIN SMALL LETTER E, U+0301 COMBINING ACUTE ACCENT)
- “ϴ” (U+03F4 GREEK CAPITAL THETA SYMBOL)
- “ڈ” (U+0688 ARABIC LETTER DDAL)
- “日” (U+65E5 CJK UNIFIED IDEOGRAPH-65E5)
- “ᚨ” (U+16A8 RUNIC LETTER ANSUZ A)

## See Also

### Inspecting a Character

- [isPunctuation](ispunctuation.md) — A Boolean value indicating whether this character represents punctuation.
- [isNewline](isnewline.md) — A Boolean value indicating whether this character represents a newline.
- [isWhitespace](iswhitespace.md) — A Boolean value indicating whether this character represents whitespace, including newlines.
- [isSymbol](issymbol.md) — A Boolean value indicating whether this character represents a symbol.
- [isMathSymbol](ismathsymbol.md) — A Boolean value indicating whether this character represents a symbol that naturally appears in mathematical contexts.
- [isCurrencySymbol](iscurrencysymbol.md) — A Boolean value indicating whether this character represents a currency symbol.
