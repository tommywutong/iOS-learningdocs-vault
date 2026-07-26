---
title: 'init(bitPattern:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float/init(bitpattern:)'
source_url: 'https://developer.apple.com/documentation/swift/float/init(bitpattern:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/init%28bitpattern%3A%29.json'
content_hash: 'sha256:3dedf6bfaee3b2a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

# init(bitPattern:)

<sub>Initializer</sub>

Creates a new value with the given bit pattern.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(bitPattern: UInt32)
```

## Parameters

- `bitPattern` — The integer encoding of a `Float` instance.

## Discussion

The value passed as `bitPattern` is interpreted in the binary interchange format defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## See Also

### Working with Binary Representation

- [bitPattern](bitpattern.md) — The bit pattern of the value’s encoding.
- [significandBitPattern](significandbitpattern.md) — The raw encoding of the value’s significand field.
- [significandWidth](significandwidth.md) — The number of bits required to represent the value’s significand.
- [exponentBitPattern](exponentbitpattern.md) — The raw encoding of the value’s exponent field.
- [significandBitCount](significandbitcount.md) — The available number of fractional significand bits.
- [exponentBitCount](exponentbitcount.md) — The number of bits used to represent the type’s exponent.
- [radix](radix.md) — The radix, or base of exponentiation, for a floating-point type.
- [init(sign:exponentBitPattern:significandBitPattern:)](<init(sign_exponentbitpattern_significandbitpattern_).md>) — Creates a new instance from the specified sign and bit patterns.
- [init(nan:signaling:)](<init(nan_signaling_).md>) — Creates a NaN (“not a number”) value with the specified payload.
- [Exponent](exponent-swift.typealias.md) — A type that can represent any written exponent.
- [RawSignificand](rawsignificand.md) — A type that represents the encoded significand of a value.
