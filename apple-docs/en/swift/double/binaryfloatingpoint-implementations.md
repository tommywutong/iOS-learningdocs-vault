---
title: BinaryFloatingPoint Implementations
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/double/binaryfloatingpoint-implementations
source_url: 'https://developer.apple.com/documentation/swift/double/binaryfloatingpoint-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/double/binaryfloatingpoint-implementations.json'
content_hash: 'sha256:2e0f939921386634'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Double](../double.md)

# BinaryFloatingPoint Implementations

<sub>API Collection</sub>

## Topics

### Initializers

- [init(_:)](<init(__)-1488d.md>) — Creates a new instance from the given value, rounded to the closest possible representation.
- [init(_:)](<init(__)-1oh9r.md>) — Creates a new value, rounded to the closest possible representation.
- [init(_:)](<init(__)-5h7qh.md>) — Creates a new instance that approximates the given value.
- [init(_:)](<init(__)-9z7ob.md>) — Creates a new instance that approximates the given value.
- [init(_:)](<init(__)-o1k9.md>) — Creates a new instance initialized to the given value.
- [init(exactly:)](<init(exactly_)-1h1oc.md>) — Creates a new value, if the given integer can be represented exactly.
- [init(exactly:)](<init(exactly_)-8esra.md>) — Creates a new instance from the given value, if it can be represented exactly.
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

- [random(in:)](<random(in_)-5o5ha.md>) — Returns a random value within the specified range.
- [random(in:)](<random(in_)-6idef.md>) — Returns a random value within the specified range.
- [random(in:using:)](<random(in_using_)-1m6gd.md>) — Returns a random value within the specified range, using the given generator as a source for randomness.
- [random(in:using:)](<random(in_using_)-613hz.md>) — Returns a random value within the specified range, using the given generator as a source for randomness.
