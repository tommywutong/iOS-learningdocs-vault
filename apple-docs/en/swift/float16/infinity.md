---
title: infinity
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float16/infinity
source_url: 'https://developer.apple.com/documentation/swift/float16/infinity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/infinity.json'
content_hash: 'sha256:a1e3d826448701a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# infinity

<sub>Type Property</sub>

Positive infinity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var infinity: Float16 { get }
```

## Discussion

Infinity compares greater than all finite numbers and equal to other infinite values.

```swift
let x = Double.greatestFiniteMagnitude
let y = x * 2
// y == Double.infinity
// y > x
```
