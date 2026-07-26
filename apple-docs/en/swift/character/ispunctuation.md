---
title: isPunctuation
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/character/ispunctuation
source_url: 'https://developer.apple.com/documentation/swift/character/ispunctuation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/character/ispunctuation.json'
content_hash: 'sha256:8c50681bafd992a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Character](../character.md)

# isPunctuation

<sub>Instance Property</sub>

A Boolean value indicating whether this character represents punctuation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isPunctuation: Bool { get }
```

## Discussion

For example, the following characters all represent punctuation:

- “!” (U+0021 EXCLAMATION MARK)
- “؟” (U+061F ARABIC QUESTION MARK)
- “…” (U+2026 HORIZONTAL ELLIPSIS)
- “—” (U+2014 EM DASH)
- ““” (U+201C LEFT DOUBLE QUOTATION MARK)

## See Also

### Inspecting a Character

- [isLetter](isletter.md) — A Boolean value indicating whether this character is a letter.
- [isNewline](isnewline.md) — A Boolean value indicating whether this character represents a newline.
- [isWhitespace](iswhitespace.md) — A Boolean value indicating whether this character represents whitespace, including newlines.
- [isSymbol](issymbol.md) — A Boolean value indicating whether this character represents a symbol.
- [isMathSymbol](ismathsymbol.md) — A Boolean value indicating whether this character represents a symbol that naturally appears in mathematical contexts.
- [isCurrencySymbol](iscurrencysymbol.md) — A Boolean value indicating whether this character represents a currency symbol.
