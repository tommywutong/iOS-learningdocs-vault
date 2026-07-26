---
title: binade
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float/binade
source_url: 'https://developer.apple.com/documentation/swift/float/binade'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/binade.json'
content_hash: 'sha256:bfb22abf4bce60b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

# binade

<sub>Instance Property</sub>

The floating-point value with the same sign and exponent as this value, but with a significand of 1.0.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var binade: Float { get }
```

## Discussion

A _binade_ is a set of binary floating-point values that all have the same sign and exponent. The `binade` property is a member of the same binade as this value, but with a unit significand.

In this example, `x` has a value of `21.5`, which is stored as `1.34375 * 2**4`, where `**` is exponentiation. Therefore, `x.binade` is equal to `1.0 * 2**4`, or `16.0`.

```swift
let x = 21.5
// x.significand == 1.34375
// x.exponent == 4

let y = x.binade
// y == 16.0
// y.significand == 1.0
// y.exponent == 4
```

## See Also

### Querying a Float

- [ulp](ulp.md) — The unit in the last place of this value.
- [significand](significand.md) — The significand of the floating-point value.
- [exponent](exponent-swift.property.md) — The exponent of the floating-point value.
- [nextUp](nextup.md) — The least representable value that compares greater than this value.
- [nextDown](nextdown.md) — The greatest representable value that compares less than this value.
