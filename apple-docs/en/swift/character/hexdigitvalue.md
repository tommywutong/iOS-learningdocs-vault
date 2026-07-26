---
title: hexDigitValue
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/character/hexdigitvalue
source_url: 'https://developer.apple.com/documentation/swift/character/hexdigitvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/character/hexdigitvalue.json'
content_hash: 'sha256:167397e0a46e8628'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Character](../character.md)

# hexDigitValue

<sub>Instance Property</sub>

The numeric value this character represents, if it is a hexadecimal digit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hexDigitValue: Int? { get }
```

## Discussion

Hexadecimal digits include 0-9, Latin letters a-f and A-F, and their fullwidth compatibility forms. If the character does not represent a hexadecimal digit, the value of this property is `nil`.

```swift
let chars: [Character] = ["1", "a", "Ｆ", "g"]
for ch in chars {
    print(ch, "-->", ch.hexDigitValue)
}
// Prints:
// 1 --> Optional(1)
// a --> Optional(10)
// Ｆ --> Optional(15)
// g --> nil
```

## See Also

### Checking a Character’s Numeric Properties

- [isNumber](isnumber.md) — A Boolean value indicating whether this character represents a number.
- [isWholeNumber](iswholenumber.md) — A Boolean value indicating whether this character represents a whole number.
- [wholeNumberValue](wholenumbervalue.md) — The numeric value this character represents, if it represents a whole number.
- [isHexDigit](ishexdigit.md) — A Boolean value indicating whether this character represents a hexadecimal digit.
