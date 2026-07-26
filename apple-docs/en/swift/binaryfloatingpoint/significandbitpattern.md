---
title: significandBitPattern
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/binaryfloatingpoint/significandbitpattern
source_url: 'https://developer.apple.com/documentation/swift/binaryfloatingpoint/significandbitpattern'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/binaryfloatingpoint/significandbitpattern.json'
content_hash: 'sha256:b5e90b1af44d9df9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BinaryFloatingPoint](../binaryfloatingpoint.md)

# significandBitPattern

<sub>Instance Property</sub>

The raw encoding of the value’s significand field.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var significandBitPattern: Self.RawSignificand { get }
```

## Discussion

The `significandBitPattern` property does not include the leading integral bit of the significand, even for types like `Float80` that store it explicitly.

## See Also

### Working with Binary Representation

- [binade](binade.md) — The floating-point value with the same sign and exponent as this value, but with a significand of 1.0.
- [exponentBitPattern](exponentbitpattern.md) — The raw encoding of the value’s exponent field.
- [significandWidth](significandwidth.md) — The number of bits required to represent the value’s significand.
- [exponentBitCount](exponentbitcount.md) — The number of bits used to represent the type’s exponent.
- [significandBitCount](significandbitcount.md) — The available number of fractional significand bits.
- [init(sign:exponentBitPattern:significandBitPattern:)](<init(sign_exponentbitpattern_significandbitpattern_).md>) — Creates a new instance from the specified sign and bit patterns.
- [RawExponent](rawexponent.md) — A type that represents the encoded exponent of a value.
- [RawSignificand](rawsignificand.md) — A type that represents the encoded significand of a value.
