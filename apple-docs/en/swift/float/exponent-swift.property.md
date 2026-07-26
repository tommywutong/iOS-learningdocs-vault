---
title: exponent
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float/exponent-swift.property
source_url: 'https://developer.apple.com/documentation/swift/float/exponent-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/exponent-swift.property.json'
content_hash: 'sha256:6f0b81a7f921b7a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

# exponent

<sub>Instance Property</sub>

The exponent of the floating-point value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

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

## See Also

### Querying a Float

- [ulp](ulp.md) — The unit in the last place of this value.
- [significand](significand.md) — The significand of the floating-point value.
- [nextUp](nextup.md) — The least representable value that compares greater than this value.
- [nextDown](nextdown.md) — The greatest representable value that compares less than this value.
- [binade](binade.md) — The floating-point value with the same sign and exponent as this value, but with a significand of 1.0.
