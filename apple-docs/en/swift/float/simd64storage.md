---
title: Float.SIMD64Storage
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float/simd64storage
source_url: 'https://developer.apple.com/documentation/swift/float/simd64storage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/simd64storage.json'
content_hash: 'sha256:7602a30323aae310'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

# Float.SIMD64Storage

<sub>Structure</sub>

Storage for a vector of 64 floating-point values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct SIMD64Storage
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../bitwisecopyable.md), [SIMDStorage](../simdstorage.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md)

## Topics

### Initializers

- [init()](<simd64storage/init().md>) — Creates a vector with zero in all lanes.

### Instance Properties

- [scalarCount](simd64storage/scalarcount.md) — The number of scalars, or elements, in the vector.

### Subscripts

- [subscript(_:)](<simd64storage/subscript(__).md>) — Accesses the element at the specified index.

### Type Aliases

- [Scalar](simd64storage/scalar.md)

## See Also

### SIMD-Supporting Types

- [SIMDMaskScalar](simdmaskscalar.md)
- [SIMD2Storage](simd2storage.md) — Storage for a vector of two floating-point values.
- [SIMD4Storage](simd4storage.md) — Storage for a vector of four floating-point values.
- [SIMD8Storage](simd8storage.md) — Storage for a vector of eight floating-point values.
- [SIMD16Storage](simd16storage.md) — Storage for a vector of 16 floating-point values.
- [SIMD32Storage](simd32storage.md) — Storage for a vector of 32 floating-point values.
