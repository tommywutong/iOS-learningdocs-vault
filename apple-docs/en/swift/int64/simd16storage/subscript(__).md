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
doc_path: '/documentation/swift/int64/simd16storage/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swift/int64/simd16storage/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int64/simd16storage/subscript%28_%3A%29.json'
content_hash: 'sha256:0515f9acc8f938bc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Int64](../../int64.md) · [SIMD16Storage](../simd16storage.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the element at the specified index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(index: Int) -> Int64 { get set }
```

## Parameters

- `index` — The index of the element to access. `index` must be in the range `0..<scalarCount`.
