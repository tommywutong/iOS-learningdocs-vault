---
title: SIMDStorage
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/simdstorage
source_url: 'https://developer.apple.com/documentation/swift/simdstorage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simdstorage.json'
content_hash: 'sha256:dbc6ffe4b353a245'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# SIMDStorage

<sub>Protocol</sub>

A type that can function as storage for a SIMD vector type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol SIMDStorage
```

## Overview

The `SIMDStorage` protocol defines a storage layout and provides elementwise accesses. Computational operations are defined on the `SIMD` protocol, which refines this protocol, and on the concrete types that conform to `SIMD`.

## Relationships

- **Inherited By**: [SIMD](simd.md)

- **Conforming Types**: [SIMD16Storage](double/simd16storage.md), [SIMD2Storage](double/simd2storage.md), [SIMD32Storage](double/simd32storage.md), [SIMD4Storage](double/simd4storage.md), [SIMD64Storage](double/simd64storage.md), [SIMD8Storage](double/simd8storage.md), [SIMD16Storage](float/simd16storage.md), [SIMD2Storage](float/simd2storage.md), [SIMD32Storage](float/simd32storage.md), [SIMD4Storage](float/simd4storage.md), [SIMD64Storage](float/simd64storage.md), [SIMD8Storage](float/simd8storage.md), [SIMD16Storage](float16/simd16storage.md), [SIMD2Storage](float16/simd2storage.md), [SIMD32Storage](float16/simd32storage.md), [SIMD4Storage](float16/simd4storage.md), [SIMD64Storage](float16/simd64storage.md), [SIMD8Storage](float16/simd8storage.md), [SIMD16Storage](int/simd16storage.md), [SIMD2Storage](int/simd2storage.md), [SIMD32Storage](int/simd32storage.md), [SIMD4Storage](int/simd4storage.md), [SIMD64Storage](int/simd64storage.md), [SIMD8Storage](int/simd8storage.md), [SIMD16Storage](int16/simd16storage.md), [SIMD2Storage](int16/simd2storage.md), [SIMD32Storage](int16/simd32storage.md), [SIMD4Storage](int16/simd4storage.md), [SIMD64Storage](int16/simd64storage.md), [SIMD8Storage](int16/simd8storage.md), [SIMD16Storage](int32/simd16storage.md), [SIMD2Storage](int32/simd2storage.md), [SIMD32Storage](int32/simd32storage.md), [SIMD4Storage](int32/simd4storage.md), [SIMD64Storage](int32/simd64storage.md), [SIMD8Storage](int32/simd8storage.md), [SIMD16Storage](int64/simd16storage.md), [SIMD2Storage](int64/simd2storage.md), [SIMD32Storage](int64/simd32storage.md), [SIMD4Storage](int64/simd4storage.md), [SIMD64Storage](int64/simd64storage.md), [SIMD8Storage](int64/simd8storage.md), [SIMD16Storage](int8/simd16storage.md), [SIMD2Storage](int8/simd2storage.md), [SIMD32Storage](int8/simd32storage.md), [SIMD4Storage](int8/simd4storage.md), [SIMD64Storage](int8/simd64storage.md), [SIMD8Storage](int8/simd8storage.md), [SIMD16](simd16.md), [SIMD2](simd2.md), [SIMD3](simd3.md), [SIMD32](simd32.md), [SIMD4](simd4.md), [SIMD64](simd64.md), [SIMD8](simd8.md), [SIMDMask](simdmask.md), [SIMD16Storage](uint/simd16storage.md), [SIMD2Storage](uint/simd2storage.md), [SIMD32Storage](uint/simd32storage.md), [SIMD4Storage](uint/simd4storage.md), [SIMD64Storage](uint/simd64storage.md), [SIMD8Storage](uint/simd8storage.md), [SIMD16Storage](uint16/simd16storage.md), [SIMD2Storage](uint16/simd2storage.md), [SIMD32Storage](uint16/simd32storage.md), [SIMD4Storage](uint16/simd4storage.md), [SIMD64Storage](uint16/simd64storage.md), [SIMD8Storage](uint16/simd8storage.md), [SIMD16Storage](uint32/simd16storage.md), [SIMD2Storage](uint32/simd2storage.md), [SIMD32Storage](uint32/simd32storage.md), [SIMD4Storage](uint32/simd4storage.md), [SIMD64Storage](uint32/simd64storage.md), [SIMD8Storage](uint32/simd8storage.md), [SIMD16Storage](uint64/simd16storage.md), [SIMD2Storage](uint64/simd2storage.md), [SIMD32Storage](uint64/simd32storage.md), [SIMD4Storage](uint64/simd4storage.md), [SIMD64Storage](uint64/simd64storage.md), [SIMD8Storage](uint64/simd8storage.md), [SIMD16Storage](uint8/simd16storage.md), [SIMD2Storage](uint8/simd2storage.md), [SIMD32Storage](uint8/simd32storage.md), [SIMD4Storage](uint8/simd4storage.md), [SIMD64Storage](uint8/simd64storage.md), [SIMD8Storage](uint8/simd8storage.md)

## Topics

### Associated Types

- [Scalar](simdstorage/scalar.md)

### Initializers

- [init()](<simdstorage/init().md>) — Creates a vector with zero in all lanes.

### Instance Properties

- [scalarCount](simdstorage/scalarcount.md) — The number of scalars, or elements, in the vector.

### Subscripts

- [subscript(_:)](<simdstorage/subscript(__).md>) — Accesses the element at the specified index.

## See Also

### Supporting Types

- [SIMD](simd.md) — A SIMD vector of a fixed number of elements.
- [SIMDScalar](simdscalar.md) — A type that can be used as an element in a SIMD vector.
- [SIMDMask](simdmask.md)
