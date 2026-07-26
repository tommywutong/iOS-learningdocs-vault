---
title: UInt.SIMD8Storage
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/uint/simd8storage
source_url: 'https://developer.apple.com/documentation/swift/uint/simd8storage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint/simd8storage.json'
content_hash: 'sha256:bbbe59d59fcf94cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt](../uint.md)

# UInt.SIMD8Storage

<sub>Structure</sub>

Storage for a vector of eight integers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct SIMD8Storage
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../bitwisecopyable.md), [SIMDStorage](../simdstorage.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md)

## Topics

### Initializers

- [init()](<simd8storage/init().md>) — Creates a vector with zero in all lanes.

### Instance Properties

- [scalarCount](simd8storage/scalarcount.md) — The number of scalars, or elements, in the vector.

### Subscripts

- [subscript(_:)](<simd8storage/subscript(__).md>) — Accesses the element at the specified index.

### Type Aliases

- [Scalar](simd8storage/scalar.md)
