---
title: 'init(sign:exponentBitPattern:significandBitPattern:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float/init(sign:exponentbitpattern:significandbitpattern:)'
source_url: 'https://developer.apple.com/documentation/swift/float/init(sign:exponentbitpattern:significandbitpattern:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/init%28sign%3Aexponentbitpattern%3Asignificandbitpattern%3A%29.json'
content_hash: 'sha256:b4aea50fe9caaa16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

# init(sign:exponentBitPattern:significandBitPattern:)

<sub>Initializer</sub>

Creates a new instance from the specified sign and bit patterns.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(sign: FloatingPointSign, exponentBitPattern: UInt, significandBitPattern: UInt32)
```

## Parameters

- `sign` — The sign of the new value.

- `exponentBitPattern` — The bit pattern to use for the exponent field of the new value.

- `significandBitPattern` — The bit pattern to use for the significand field of the new value.

## Discussion

The values passed as `exponentBitPattern` and `significandBitPattern` are interpreted in the binary interchange format defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## See Also

### Working with Binary Representation

- [bitPattern](bitpattern.md) — The bit pattern of the value’s encoding.
- [significandBitPattern](significandbitpattern.md) — The raw encoding of the value’s significand field.
- [significandWidth](significandwidth.md) — The number of bits required to represent the value’s significand.
- [exponentBitPattern](exponentbitpattern.md) — The raw encoding of the value’s exponent field.
- [significandBitCount](significandbitcount.md) — The available number of fractional significand bits.
- [exponentBitCount](exponentbitcount.md) — The number of bits used to represent the type’s exponent.
- [radix](radix.md) — The radix, or base of exponentiation, for a floating-point type.
- [init(bitPattern:)](<init(bitpattern_).md>) — Creates a new value with the given bit pattern.
- [init(nan:signaling:)](<init(nan_signaling_).md>) — Creates a NaN (“not a number”) value with the specified payload.
- [Exponent](exponent-swift.typealias.md) — A type that can represent any written exponent.
- [RawSignificand](rawsignificand.md) — A type that represents the encoded significand of a value.
