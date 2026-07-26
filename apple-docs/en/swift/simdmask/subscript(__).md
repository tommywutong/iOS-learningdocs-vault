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
doc_path: '/documentation/swift/simdmask/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swift/simdmask/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simdmask/subscript%28_%3A%29.json'
content_hash: 'sha256:7f1c944b68eebbbd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMDMask](../simdmask.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the element at the specified index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(index: Int) -> Bool { get set }
```

## Parameters

- `index` — The index of the element to access. `index` must be in the range `0..<scalarCount`.
