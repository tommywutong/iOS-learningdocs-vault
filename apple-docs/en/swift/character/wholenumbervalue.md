---
title: wholeNumberValue
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/character/wholenumbervalue
source_url: 'https://developer.apple.com/documentation/swift/character/wholenumbervalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/character/wholenumbervalue.json'
content_hash: 'sha256:f390aff78636fe99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Character](../character.md)

# wholeNumberValue

<sub>Instance Property</sub>

The numeric value this character represents, if it represents a whole number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var wholeNumberValue: Int? { get }
```

## Discussion

If this character does not represent a whole number, or the value is too large to represent as an `Int`, the value of this property is `nil`.

```swift
let chars: [Character] = ["4", "④", "万", "a"]
for ch in chars {
    print(ch, "-->", ch.wholeNumberValue)
}
// Prints:
// 4 --> Optional(4)
// ④ --> Optional(4)
// 万 --> Optional(10000)
// a --> nil
```

## See Also

### Checking a Character’s Numeric Properties

- [isNumber](isnumber.md) — A Boolean value indicating whether this character represents a number.
- [isWholeNumber](iswholenumber.md) — A Boolean value indicating whether this character represents a whole number.
- [isHexDigit](ishexdigit.md) — A Boolean value indicating whether this character represents a hexadecimal digit.
- [hexDigitValue](hexdigitvalue.md) — The numeric value this character represents, if it is a hexadecimal digit.
