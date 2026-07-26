---
title: isHexDigit
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/character/ishexdigit
source_url: 'https://developer.apple.com/documentation/swift/character/ishexdigit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/character/ishexdigit.json'
content_hash: 'sha256:9a47bb4505e87649'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Character](../character.md)

# isHexDigit

<sub>Instance Property</sub>

A Boolean value indicating whether this character represents a hexadecimal digit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isHexDigit: Bool { get }
```

## Discussion

Hexadecimal digits include 0-9, Latin letters a-f and A-F, and their fullwidth compatibility forms. To get the character’s value, use the `hexDigitValue` property.

## See Also

### Checking a Character’s Numeric Properties

- [isNumber](isnumber.md) — A Boolean value indicating whether this character represents a number.
- [isWholeNumber](iswholenumber.md) — A Boolean value indicating whether this character represents a whole number.
- [wholeNumberValue](wholenumbervalue.md) — The numeric value this character represents, if it represents a whole number.
- [hexDigitValue](hexdigitvalue.md) — The numeric value this character represents, if it is a hexadecimal digit.
