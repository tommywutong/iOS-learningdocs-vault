---
title: isMathSymbol
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/character/ismathsymbol
source_url: 'https://developer.apple.com/documentation/swift/character/ismathsymbol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/character/ismathsymbol.json'
content_hash: 'sha256:80d829756037ce4c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Character](../character.md)

# isMathSymbol

<sub>Instance Property</sub>

A Boolean value indicating whether this character represents a symbol that naturally appears in mathematical contexts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isMathSymbol: Bool { get }
```

## Discussion

For example, the following characters all represent math symbols:

- “+” (U+002B PLUS SIGN)
- “∫” (U+222B INTEGRAL)
- “ϰ” (U+03F0 GREEK KAPPA SYMBOL)

The set of characters that have an `isMathSymbol` value of `true` is not a strict subset of those for which `isSymbol` is `true`. This includes characters used both as letters and commonly in mathematical formulas. For example, “ϰ” (U+03F0 GREEK KAPPA SYMBOL) is considered both a mathematical symbol and a letter.

This property corresponds to the “Math” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).

## See Also

### Inspecting a Character

- [isLetter](isletter.md) — A Boolean value indicating whether this character is a letter.
- [isPunctuation](ispunctuation.md) — A Boolean value indicating whether this character represents punctuation.
- [isNewline](isnewline.md) — A Boolean value indicating whether this character represents a newline.
- [isWhitespace](iswhitespace.md) — A Boolean value indicating whether this character represents whitespace, including newlines.
- [isSymbol](issymbol.md) — A Boolean value indicating whether this character represents a symbol.
- [isCurrencySymbol](iscurrencysymbol.md) — A Boolean value indicating whether this character represents a currency symbol.
