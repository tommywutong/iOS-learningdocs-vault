---
title: isFinite
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/isfinite
source_url: 'https://developer.apple.com/documentation/swift/float80/isfinite'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/isfinite.json'
content_hash: 'sha256:90af1cd57a03642d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# isFinite

<sub>Instance Property</sub>

A Boolean value indicating whether this instance is finite.

<sub>macOS</sub>

```swift
var isFinite: Bool { get }
```

## Discussion

All values other than NaN and infinity are considered finite, whether normal or subnormal.  For NaN, both `isFinite` and `isInfinite` are false.
