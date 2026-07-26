---
title: infinity
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/infinity
source_url: 'https://developer.apple.com/documentation/swift/float80/infinity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/infinity.json'
content_hash: 'sha256:ad82352dbe158a79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# infinity

<sub>Type Property</sub>

Positive infinity.

<sub>macOS</sub>

```swift
static var infinity: Float80 { get }
```

## Discussion

Infinity compares greater than all finite numbers and equal to other infinite values.

```swift
let x = Double.greatestFiniteMagnitude
let y = x * 2
// y == Double.infinity
// y > x
```
