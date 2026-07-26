---
title: SIMD Implementations
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/simdmask/simd-implementations
source_url: 'https://developer.apple.com/documentation/swift/simdmask/simd-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simdmask/simd-implementations.json'
content_hash: 'sha256:b4cdca8943628c64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Numbers and Basic Values](../numbers-and-basic-values.md) · [SIMD Vector Types](../simd-vector-types.md) · [SIMDMask](../simdmask.md)

# SIMD Implementations

<sub>API Collection</sub>

## Topics

### Operators

- [.!=(_:_:)](<'.!=(____)-4o6ac.md>) — Returns a vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<'.!=(____)-5cnom.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<'.!=(____)-94n12.md>) — Returns a vector mask with the result of a pointwise inequality comparison.
- [.==(_:_:)](<'.==(____)-4l749.md>) — Returns a vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<'.==(____)-6aq3z.md>) — Returns a vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<'.==(____)-8vdyh.md>) — A vector mask with the result of a pointwise equality comparison.
- [==(_:_:)](<==(____).md>) — Returns a Boolean value indicating whether two vectors are equal.

### Initializers

- [init(_:)](<init(__).md>) — Creates a vector from the given sequence.
- [init(arrayLiteral:)](<init(arrayliteral_).md>) — Creates a vector from the specified elements.
- [init(from:)](<init(from_).md>) — Creates a new vector by decoding scalars from the given decoder.
- [init(repeating:)](<init(repeating_)-5pwub.md>) — A vector with the specified scalar in all lanes.

### Instance Properties

- [description](description.md) — A textual description of the vector.
- [indices](indices.md) — The valid indices for subscripting the vector.

### Instance Methods

- [encode(to:)](<encode(to_).md>) — Encodes the scalars of this vector into the given encoder in an unkeyed container.
- [hash(into:)](<hash(into_).md>) — Hashes the elements of the vector using the given hasher.
- [replace(with:where:)](<replace(with_where_)-6wonx.md>) — Replaces elements of this vector with `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<replace(with_where_)-7bhx.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<replacing(with_where_)-2gka4.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<replacing(with_where_)-3lyjl.md>) — Returns a copy of this vector, with elements `other` in the lanes where `mask` is `true`.
