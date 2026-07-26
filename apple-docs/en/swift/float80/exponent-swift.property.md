---
title: exponent
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/exponent-swift.property
source_url: 'https://developer.apple.com/documentation/swift/float80/exponent-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/exponent-swift.property.json'
content_hash: 'sha256:4b3ae427b0f2309a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# exponent

<sub>Instance Property</sub>

The exponent of the floating-point value.

<sub>macOS</sub>

```swift
var exponent: Int { get }
```

## Discussion

The _exponent_ of a floating-point value is the integer part of the logarithm of the value’s magnitude. For a value `x` of a floating-point type `F`, the magnitude can be calculated as the following, where `**` is exponentiation:

```swift
x.significand * (F.radix ** x.exponent)
```

In the next example, `y` has a value of `21.5`, which is encoded as `1.34375 * 2 ** 4`. The significand of `y` is therefore 1.34375.

```swift
let y: Double = 21.5
// y.significand == 1.34375
// y.exponent == 4
// Double.radix == 2
```

The `exponent` property has the following edge cases:

- If `x` is zero, then `x.exponent` is `Int.min`.
- If `x` is +/-infinity or NaN, then `x.exponent` is `Int.max`

This property implements the `logB` operation defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).
