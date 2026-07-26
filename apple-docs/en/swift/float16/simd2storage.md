---
title: Float16.SIMD2Storage
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float16/simd2storage
source_url: 'https://developer.apple.com/documentation/swift/float16/simd2storage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/simd2storage.json'
content_hash: 'sha256:6dadd61ff42caa03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# Float16.SIMD2Storage

<sub>Structure</sub>

Storage for a vector of two floating-point values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct SIMD2Storage
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../bitwisecopyable.md), [SIMDStorage](../simdstorage.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md)

## Topics

### Initializers

- [init()](<simd2storage/init().md>) — Creates a vector with zero in all lanes.

### Instance Properties

- [scalarCount](simd2storage/scalarcount.md) — The number of scalars, or elements, in the vector.

### Subscripts

- [subscript(_:)](<simd2storage/subscript(__).md>) — Accesses the element at the specified index.

### Type Aliases

- [Scalar](simd2storage/scalar.md)
