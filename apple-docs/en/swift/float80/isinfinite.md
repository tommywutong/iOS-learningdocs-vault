---
title: isInfinite
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/isinfinite
source_url: 'https://developer.apple.com/documentation/swift/float80/isinfinite'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/isinfinite.json'
content_hash: 'sha256:649616415ae36940'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# isInfinite

<sub>Instance Property</sub>

A Boolean value indicating whether the instance is infinite.

<sub>macOS</sub>

```swift
var isInfinite: Bool { get }
```

## Discussion

For NaN, both `isFinite` and `isInfinite` are false.
