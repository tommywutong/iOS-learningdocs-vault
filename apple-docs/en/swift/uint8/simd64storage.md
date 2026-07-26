---
title: UInt8.SIMD64Storage
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/uint8/simd64storage
source_url: 'https://developer.apple.com/documentation/swift/uint8/simd64storage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint8/simd64storage.json'
content_hash: 'sha256:5f714f8d319f1769'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt8](../uint8.md)

# UInt8.SIMD64Storage

<sub>Structure</sub>

Storage for a vector of 64 integers.

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
