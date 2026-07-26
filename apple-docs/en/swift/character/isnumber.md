---
title: isNumber
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/character/isnumber
source_url: 'https://developer.apple.com/documentation/swift/character/isnumber'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/character/isnumber.json'
content_hash: 'sha256:880c94d7a8246efb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Character](../character.md)

# isNumber

<sub>Instance Property</sub>

A Boolean value indicating whether this character represents a number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isNumber: Bool { get }
```

## Discussion

For example, the following characters all represent numbers:

- “7” (U+0037 DIGIT SEVEN)
- “⅚” (U+215A VULGAR FRACTION FIVE SIXTHS)
- “㊈” (U+3288 CIRCLED IDEOGRAPH NINE)
- “𝟠” (U+1D7E0 MATHEMATICAL DOUBLE-STRUCK DIGIT EIGHT)
- “๒” (U+0E52 THAI DIGIT TWO)

## See Also

### Checking a Character’s Numeric Properties

- [isWholeNumber](iswholenumber.md) — A Boolean value indicating whether this character represents a whole number.
- [wholeNumberValue](wholenumbervalue.md) — The numeric value this character represents, if it represents a whole number.
- [isHexDigit](ishexdigit.md) — A Boolean value indicating whether this character represents a hexadecimal digit.
- [hexDigitValue](hexdigitvalue.md) — The numeric value this character represents, if it is a hexadecimal digit.
