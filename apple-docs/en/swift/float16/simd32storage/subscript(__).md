---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float16/simd32storage/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swift/float16/simd32storage/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/simd32storage/subscript%28_%3A%29.json'
content_hash: 'sha256:4a26898dbeca8df5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Float16](../../float16.md) · [SIMD32Storage](../simd32storage.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the element at the specified index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(index: Int) -> Float16 { get set }
```

## Parameters

- `index` — The index of the element to access. `index` must be in the range `0..<scalarCount`.
