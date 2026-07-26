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
doc_path: '/documentation/swift/uint64/simd2storage/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swift/uint64/simd2storage/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint64/simd2storage/subscript%28_%3A%29.json'
content_hash: 'sha256:0feb18a2c907a122'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [UInt64](../../uint64.md) · [SIMD2Storage](../simd2storage.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the element at the specified index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(index: Int) -> UInt64 { get set }
```

## Parameters

- `index` — The index of the element to access. `index` must be in the range `0..<scalarCount`.
