---
title: binade
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/binaryfloatingpoint/binade
source_url: 'https://developer.apple.com/documentation/swift/binaryfloatingpoint/binade'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/binaryfloatingpoint/binade.json'
content_hash: 'sha256:4b416756ed12f57f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BinaryFloatingPoint](../binaryfloatingpoint.md)

# binade

<sub>Instance Property</sub>

The floating-point value with the same sign and exponent as this value, but with a significand of 1.0.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var binade: Self { get }
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

### Working with Binary Representation

- [exponentBitPattern](exponentbitpattern.md) — The raw encoding of the value’s exponent field.
- [significandBitPattern](significandbitpattern.md) — The raw encoding of the value’s significand field.
- [significandWidth](significandwidth.md) — The number of bits required to represent the value’s significand.
- [exponentBitCount](exponentbitcount.md) — The number of bits used to represent the type’s exponent.
- [significandBitCount](significandbitcount.md) — The available number of fractional significand bits.
- [init(sign:exponentBitPattern:significandBitPattern:)](<init(sign_exponentbitpattern_significandbitpattern_).md>) — Creates a new instance from the specified sign and bit patterns.
- [RawExponent](rawexponent.md) — A type that represents the encoded exponent of a value.
- [RawSignificand](rawsignificand.md) — A type that represents the encoded significand of a value.
