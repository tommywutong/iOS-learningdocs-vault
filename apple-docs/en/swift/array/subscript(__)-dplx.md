---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/array/subscript(_:)-dplx'
source_url: 'https://developer.apple.com/documentation/swift/array/subscript(_:)-dplx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/subscript%28_%3A%29-dplx.json'
content_hash: 'sha256:da7a202dc1da079d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns the first metric whose `Metric/name` equals the given metric’s name, or `nil` if not found.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
subscript(metric: Metric) -> Metric? { get }
```
