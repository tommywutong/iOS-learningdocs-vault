---
title: isNewline
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/character/isnewline
source_url: 'https://developer.apple.com/documentation/swift/character/isnewline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/character/isnewline.json'
content_hash: 'sha256:8326f6ec176c2fcc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Character](../character.md)

# isNewline

<sub>Instance Property</sub>

A Boolean value indicating whether this character represents a newline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isNewline: Bool { get }
```

## Discussion

For example, the following characters all represent newlines:

- “\\n” (U+000A): LINE FEED (LF)
- U+000B: LINE TABULATION (VT)
- U+000C: FORM FEED (FF)
- “\\r” (U+000D): CARRIAGE RETURN (CR)
- “\\r\\n” (U+000D U+000A): CR-LF
- U+0085: NEXT LINE (NEL)
- U+2028: LINE SEPARATOR
- U+2029: PARAGRAPH SEPARATOR

## See Also

### Inspecting a Character

- [isLetter](isletter.md) — A Boolean value indicating whether this character is a letter.
- [isPunctuation](ispunctuation.md) — A Boolean value indicating whether this character represents punctuation.
- [isWhitespace](iswhitespace.md) — A Boolean value indicating whether this character represents whitespace, including newlines.
- [isSymbol](issymbol.md) — A Boolean value indicating whether this character represents a symbol.
- [isMathSymbol](ismathsymbol.md) — A Boolean value indicating whether this character represents a symbol that naturally appears in mathematical contexts.
- [isCurrencySymbol](iscurrencysymbol.md) — A Boolean value indicating whether this character represents a currency symbol.
