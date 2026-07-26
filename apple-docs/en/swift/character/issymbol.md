---
title: isSymbol
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/character/issymbol
source_url: 'https://developer.apple.com/documentation/swift/character/issymbol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/character/issymbol.json'
content_hash: 'sha256:5dcebf431da9c7b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Character](../character.md)

# isSymbol

<sub>Instance Property</sub>

A Boolean value indicating whether this character represents a symbol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isSymbol: Bool { get }
```

## Discussion

This property is `true` only for characters composed of scalars in the “Math_Symbol”, “Currency_Symbol”, “Modifier_Symbol”, or “Other_Symbol” categories in the [Unicode Standard](https://unicode.org/reports/tr44/#General_Category_Values).

For example, the following characters all represent symbols:

- “®” (U+00AE REGISTERED SIGN)
- “⌹” (U+2339 APL FUNCTIONAL SYMBOL QUAD DIVIDE)
- “⡆” (U+2846 BRAILLE PATTERN DOTS-237)

## See Also

### Inspecting a Character

- [isLetter](isletter.md) — A Boolean value indicating whether this character is a letter.
- [isPunctuation](ispunctuation.md) — A Boolean value indicating whether this character represents punctuation.
- [isNewline](isnewline.md) — A Boolean value indicating whether this character represents a newline.
- [isWhitespace](iswhitespace.md) — A Boolean value indicating whether this character represents whitespace, including newlines.
- [isMathSymbol](ismathsymbol.md) — A Boolean value indicating whether this character represents a symbol that naturally appears in mathematical contexts.
- [isCurrencySymbol](iscurrencysymbol.md) — A Boolean value indicating whether this character represents a currency symbol.
