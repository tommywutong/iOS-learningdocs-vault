---
title: Int.SIMD32Storage
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int/simd32storage
source_url: 'https://developer.apple.com/documentation/swift/int/simd32storage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int/simd32storage.json'
content_hash: 'sha256:aa93ec0bd5d46464'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int](../int.md)

# Int.SIMD32Storage

<sub>Structure</sub>

Storage for a vector of 32 integers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct SIMD32Storage
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../bitwisecopyable.md), [SIMDStorage](../simdstorage.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md)

## Topics

### Initializers

- [init()](<simd32storage/init().md>) — Creates a vector with zero in all lanes.

### Instance Properties

- [scalarCount](simd32storage/scalarcount.md) — The number of scalars, or elements, in the vector.

### Subscripts

- [subscript(_:)](<simd32storage/subscript(__).md>) — Accesses the element at the specified index.

### Type Aliases

- [Scalar](simd32storage/scalar.md)

## See Also

### SIMD-Supporting Types

- [SIMDMaskScalar](simdmaskscalar.md)
- [SIMD2Storage](simd2storage.md) — Storage for a vector of two integers.
- [SIMD4Storage](simd4storage.md) — Storage for a vector of four integers.
- [SIMD8Storage](simd8storage.md) — Storage for a vector of eight integers.
- [SIMD16Storage](simd16storage.md) — Storage for a vector of 16 integers.
- [SIMD64Storage](simd64storage.md) — Storage for a vector of 64 integers.
