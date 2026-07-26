---
title: isCurrencySymbol
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/character/iscurrencysymbol
source_url: 'https://developer.apple.com/documentation/swift/character/iscurrencysymbol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/character/iscurrencysymbol.json'
content_hash: 'sha256:30f88271ebf1d89b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Character](../character.md)

# isCurrencySymbol

<sub>Instance Property</sub>

A Boolean value indicating whether this character represents a currency symbol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isCurrencySymbol: Bool { get }
```

## Discussion

For example, the following characters all represent currency symbols:

- “$” (U+0024 DOLLAR SIGN)
- “¥” (U+00A5 YEN SIGN)
- “€” (U+20AC EURO SIGN)

## See Also

### Inspecting a Character

- [isLetter](isletter.md) — A Boolean value indicating whether this character is a letter.
- [isPunctuation](ispunctuation.md) — A Boolean value indicating whether this character represents punctuation.
- [isNewline](isnewline.md) — A Boolean value indicating whether this character represents a newline.
- [isWhitespace](iswhitespace.md) — A Boolean value indicating whether this character represents whitespace, including newlines.
- [isSymbol](issymbol.md) — A Boolean value indicating whether this character represents a symbol.
- [isMathSymbol](ismathsymbol.md) — A Boolean value indicating whether this character represents a symbol that naturally appears in mathematical contexts.
