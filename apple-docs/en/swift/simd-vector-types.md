---
title: SIMD Vector Types
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/simd-vector-types
source_url: 'https://developer.apple.com/documentation/swift/simd-vector-types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd-vector-types.json'
content_hash: 'sha256:4990b5141030ac32'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md) · [Swift Standard Library](swift-standard-library.md) · [Numbers and Basic Values](numbers-and-basic-values.md)

# SIMD Vector Types

<sub>API Collection</sub>

Work with fixed-width vectors of fixed-width numeric types of different sizes.

## Topics

### SIMD Vectors

- [SIMD2](simd2.md) — A vector of two scalar values.
- [SIMD3](simd3.md) — A vector of three scalar values.
- [SIMD4](simd4.md) — A vector of four scalar values.
- [SIMD8](simd8.md) — A vector of eight scalar values.
- [SIMD16](simd16.md) — A vector of 16 scalar values.
- [SIMD32](simd32.md) — A vector of 32 scalar values.
- [SIMD64](simd64.md) — A vector of 64 scalar values.

### Supporting Types

- [SIMD](simd.md) — A SIMD vector of a fixed number of elements.
- [SIMDScalar](simdscalar.md) — A type that can be used as an element in a SIMD vector.
- [SIMDStorage](simdstorage.md) — A type that can function as storage for a SIMD vector type.
- [SIMDMask](simdmask.md)

### Supporting Functions

- [all(_:)](<all(__).md>) — True if every lane of mask is true.
- [any(_:)](<any(__).md>) — True if any lane of mask is true.
- [pointwiseMax(_:_:)](<pointwisemax(____)-29hn2.md>) — The lanewise maximum of two vectors.
- [pointwiseMax(_:_:)](<pointwisemax(____)-2k6er.md>) — The lanewise maximum of two vectors.
- [pointwiseMin(_:_:)](<pointwisemin(____)-39txi.md>) — The lanewise minimum of two vectors.
- [pointwiseMin(_:_:)](<pointwisemin(____)-8v95p.md>) — The lanewise minimum of two vectors.

## See Also

### Advanced Numerics

- [Numeric Protocols](numeric-protocols.md) — Write generic code that works with any numeric type.
- [Special-Use Numeric Types](special-use-numeric-types.md) — Work with fixed-width numeric types of different sizes.
- [Global Numeric Functions](global-numeric-functions.md) — Use these functions with numeric values and other comparable types.
