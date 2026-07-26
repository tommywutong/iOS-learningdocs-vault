---
title: 'init(nan:signaling:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float/init(nan:signaling:)'
source_url: 'https://developer.apple.com/documentation/swift/float/init(nan:signaling:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/init%28nan%3Asignaling%3A%29.json'
content_hash: 'sha256:acb2180a86fe5550'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

# init(nan:signaling:)

<sub>Initializer</sub>

Creates a NaN (“not a number”) value with the specified payload.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(nan payload: Float.RawSignificand, signaling: Bool)
```

## Parameters

- `payload` — The payload to use for the new NaN value.

- `signaling` — Pass `true` to create a signaling NaN or `false` to create a quiet NaN.

## Discussion

NaN values compare not equal to every value, including themselves. Most operations with a NaN operand produce a NaN result. Don’t use the equal-to operator (`==`) to test whether a value is NaN. Instead, use the value’s `isNaN` property.

```swift
let x = Float(nan: 0, signaling: false)
print(x == .nan)
// Prints "false"
print(x.isNaN)
// Prints "true"
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
- [Exponent](exponent-swift.typealias.md) — A type that can represent any written exponent.
- [RawSignificand](rawsignificand.md) — A type that represents the encoded significand of a value.
