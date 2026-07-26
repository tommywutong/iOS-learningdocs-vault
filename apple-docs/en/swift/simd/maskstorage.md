---
title: MaskStorage
framework: Swift
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/simd/maskstorage
source_url: 'https://developer.apple.com/documentation/swift/simd/maskstorage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd/maskstorage.json'
content_hash: 'sha256:3f4e8bf5f9acff5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD](../simd.md)

# MaskStorage

<sub>Associated Type</sub>

The mask type resulting from pointwise comparisons of this vector type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype MaskStorage : SIMD where Self.MaskStorage.Scalar : FixedWidthInteger, Self.MaskStorage.Scalar : SignedInteger
```
