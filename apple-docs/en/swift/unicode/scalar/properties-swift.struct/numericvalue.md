---
title: numericValue
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/numericvalue
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/numericvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/numericvalue.json'
content_hash: 'sha256:7bf9807a6e2911b3'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# numericValue

<sub>Instance Property</sub>

The numeric value of the scalar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var numericValue: Double? { get }
```

## Discussion

For scalars that represent a numeric value, `numericValue` is the whole or fractional value. For all other scalars, this property is `nil`.

```swift
let scalars: [Unicode.Scalar] = ["4", "④", "⅕", "X"]
for scalar in scalars {
    print(scalar, "-->", scalar.properties.numericValue)
}
// 4 --> Optional(4.0)
// ④ --> Optional(4.0)
// ⅕ --> Optional(0.2)
// X --> nil
```

This property corresponds to the “Numeric_Value” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).
