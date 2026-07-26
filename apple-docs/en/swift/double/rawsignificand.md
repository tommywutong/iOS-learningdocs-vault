---
title: Double.RawSignificand
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/double/rawsignificand
source_url: 'https://developer.apple.com/documentation/swift/double/rawsignificand'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/double/rawsignificand.json'
content_hash: 'sha256:be02980191be81a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Double](../double.md)

# Double.RawSignificand

<sub>Type Alias</sub>

A type that represents the encoded significand of a value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias RawSignificand = UInt64
```

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
- [init(sign:exponentBitPattern:significandBitPattern:)](<init(sign_exponentbitpattern_significandbitpattern_).md>) — Creates a new instance from the specified sign and bit patterns.
- [init(nan:signaling:)](<init(nan_signaling_).md>) — Creates a NaN (“not a number”) value with the specified payload.
- [Exponent](exponent-swift.typealias.md) — A type that can represent any written exponent.
- [RawExponent](rawexponent.md) — A type that represents the encoded exponent of a value.
