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
doc_path: '/documentation/swift/int8/simd2storage/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swift/int8/simd2storage/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int8/simd2storage/subscript%28_%3A%29.json'
content_hash: 'sha256:5fe83b373dfdc7d3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Int8](../../int8.md) · [SIMD2Storage](../simd2storage.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the element at the specified index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(index: Int) -> Int8 { get set }
```

## Parameters

- `index` — The index of the element to access. `index` must be in the range `0..<scalarCount`.
