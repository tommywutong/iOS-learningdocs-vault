---
title: BinaryFloatingPoint Implementations
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float16/binaryfloatingpoint-implementations
source_url: 'https://developer.apple.com/documentation/swift/float16/binaryfloatingpoint-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/binaryfloatingpoint-implementations.json'
content_hash: 'sha256:8933361ea8181be1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Numbers and Basic Values](../numbers-and-basic-values.md) · [Special-Use Numeric Types](../special-use-numeric-types.md) · [Float16](../float16.md)

# BinaryFloatingPoint Implementations

<sub>API Collection</sub>

## Topics

### Initializers

- [init(_:)](<init(__)-469bw.md>) — Creates a new instance that approximates the given value.
- [init(_:)](<init(__)-6u8fq.md>) — Creates a new instance from the given value, rounded to the closest possible representation.
- [init(_:)](<init(__)-7teyd.md>) — Creates a new value, rounded to the closest possible representation.
- [init(_:)](<init(__)-7x3fq.md>) — Creates a new instance that approximates the given value.
- [init(exactly:)](<init(exactly_)-6c0t5.md>) — Creates a new value, if the given integer can be represented exactly.
- [init(exactly:)](<init(exactly_)-d42j.md>) — Creates a new instance from the given value, if it can be represented exactly.
- [init(sign:exponentBitPattern:significandBitPattern:)](<init(sign_exponentbitpattern_significandbitpattern_).md>) — Creates a new instance from the specified sign and bit patterns.

### Instance Properties

- [binade](binade.md) — The floating-point value with the same sign and exponent as this value, but with a significand of 1.0.
- [exponentBitPattern](exponentbitpattern.md) — The raw encoding of the value’s exponent field.
- [significandBitPattern](significandbitpattern.md) — The raw encoding of the value’s significand field.
- [significandWidth](significandwidth.md) — The number of bits required to represent the value’s significand.

### Type Aliases

- [RawExponent](rawexponent.md) — A type that represents the encoded exponent of a value.
- [RawSignificand](rawsignificand.md) — A type that represents the encoded significand of a value.

### Type Properties

- [exponentBitCount](exponentbitcount.md) — The number of bits used to represent the type’s exponent.
- [significandBitCount](significandbitcount.md) — The available number of fractional significand bits.

### Type Methods

- [random(in:)](<random(in_)-4blql.md>) — Returns a random value within the specified range.
- [random(in:)](<random(in_)-6nryy.md>) — Returns a random value within the specified range.
- [random(in:using:)](<random(in_using_)-1prt0.md>) — Returns a random value within the specified range, using the given generator as a source for randomness.
- [random(in:using:)](<random(in_using_)-9qt91.md>) — Returns a random value within the specified range, using the given generator as a source for randomness.
