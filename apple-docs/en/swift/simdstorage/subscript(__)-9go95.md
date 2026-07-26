---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/simdstorage/subscript(_:)-9go95'
source_url: 'https://developer.apple.com/documentation/swift/simdstorage/subscript(_:)-9go95'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simdstorage/subscript%28_%3A%29-9go95.json'
content_hash: 'sha256:0ec4abac0d48d2b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMDStorage](../simdstorage.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Extracts the scalars at specified indices to form a SIMD32.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<Index>(index: SIMD32<Index>) -> SIMD32<Self.Scalar> where Index : FixedWidthInteger, Index : SIMDScalar, Self.Scalar : SIMDScalar { get }
```

## Overview

The elements of the index vector are wrapped modulo the count of elements in this vector. Because of this, the index is always in-range and no trap can occur.
