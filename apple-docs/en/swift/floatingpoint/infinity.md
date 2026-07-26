---
title: infinity
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpoint/infinity
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/infinity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/infinity.json'
content_hash: 'sha256:cd0b627422fbe209'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

# infinity

<sub>Type Property</sub>

Positive infinity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var infinity: Self { get }
```

## Discussion

Infinity compares greater than all finite numbers and equal to other infinite values.

```swift
let x = Double.greatestFiniteMagnitude
let y = x * 2
// y == Double.infinity
// y > x
```
