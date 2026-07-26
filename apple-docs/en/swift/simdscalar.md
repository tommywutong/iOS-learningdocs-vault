---
title: SIMDScalar
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/simdscalar
source_url: 'https://developer.apple.com/documentation/swift/simdscalar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simdscalar.json'
content_hash: 'sha256:64a1d35a06cc2932'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# SIMDScalar

<sub>Protocol</sub>

A type that can be used as an element in a SIMD vector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol SIMDScalar : BitwiseCopyable
```

## Relationships

- **Inherits From**: [BitwiseCopyable](bitwisecopyable.md)

- **Conforming Types**: [Double](double.md), [Float](float.md), [Float16](float16.md), [Int](int.md), [Int16](int16.md), [Int32](int32.md), [Int64](int64.md), [Int8](int8.md), [UInt](uint.md), [UInt16](uint16.md), [UInt32](uint32.md), [UInt64](uint64.md), [UInt8](uint8.md)

## Topics

### Associated Types

- [SIMD16Storage](simdscalar/simd16storage.md)
- [SIMD2Storage](simdscalar/simd2storage.md)
- [SIMD32Storage](simdscalar/simd32storage.md)
- [SIMD4Storage](simdscalar/simd4storage.md)
- [SIMD64Storage](simdscalar/simd64storage.md)
- [SIMD8Storage](simdscalar/simd8storage.md)
- [SIMDMaskScalar](simdscalar/simdmaskscalar.md)

## See Also

### Supporting Types

- [SIMD](simd.md) — A SIMD vector of a fixed number of elements.
- [SIMDStorage](simdstorage.md) — A type that can function as storage for a SIMD vector type.
- [SIMDMask](simdmask.md)
