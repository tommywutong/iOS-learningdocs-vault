---
title: numericType
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/numerictype
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/numerictype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/numerictype.json'
content_hash: 'sha256:4b842ef0204bcc36'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# numericType

<sub>Instance Property</sub>

The numeric type of the scalar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var numericType: Unicode.NumericType? { get }
```

## Discussion

For scalars that represent a number, `numericType` is the numeric type of the scalar. For all other scalars, this property is `nil`.

```swift
let scalars: [Unicode.Scalar] = ["4", "④", "⅕", "X"]
for scalar in scalars {
    print(scalar, "-->", scalar.properties.numericType)
}
// 4 --> Optional(Swift.Unicode.NumericType.decimal)
// ④ --> Optional(Swift.Unicode.NumericType.digit)
// ⅕ --> Optional(Swift.Unicode.NumericType.numeric)
// X --> nil
```

This property corresponds to the “Numeric_Type” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).
