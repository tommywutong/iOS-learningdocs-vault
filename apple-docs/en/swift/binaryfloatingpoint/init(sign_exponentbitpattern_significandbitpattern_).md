---
title: 'init(sign:exponentBitPattern:significandBitPattern:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/binaryfloatingpoint/init(sign:exponentbitpattern:significandbitpattern:)'
source_url: 'https://developer.apple.com/documentation/swift/binaryfloatingpoint/init(sign:exponentbitpattern:significandbitpattern:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/binaryfloatingpoint/init%28sign%3Aexponentbitpattern%3Asignificandbitpattern%3A%29.json'
content_hash: 'sha256:4544ef0e3ae0a887'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BinaryFloatingPoint](../binaryfloatingpoint.md)

# init(sign:exponentBitPattern:significandBitPattern:)

<sub>Initializer</sub>

Creates a new instance from the specified sign and bit patterns.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(sign: FloatingPointSign, exponentBitPattern: Self.RawExponent, significandBitPattern: Self.RawSignificand)
```

## Parameters

- `sign` — The sign of the new value.

- `exponentBitPattern` — The bit pattern to use for the exponent field of the new value.

- `significandBitPattern` — The bit pattern to use for the significand field of the new value.

## Discussion

The values passed as `exponentBitPattern` and `significandBitPattern` are interpreted in the binary interchange format defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## See Also

### Working with Binary Representation

- [binade](binade.md) — The floating-point value with the same sign and exponent as this value, but with a significand of 1.0.
- [exponentBitPattern](exponentbitpattern.md) — The raw encoding of the value’s exponent field.
- [significandBitPattern](significandbitpattern.md) — The raw encoding of the value’s significand field.
- [significandWidth](significandwidth.md) — The number of bits required to represent the value’s significand.
- [exponentBitCount](exponentbitcount.md) — The number of bits used to represent the type’s exponent.
- [significandBitCount](significandbitcount.md) — The available number of fractional significand bits.
- [RawExponent](rawexponent.md) — A type that represents the encoded exponent of a value.
- [RawSignificand](rawsignificand.md) — A type that represents the encoded significand of a value.
