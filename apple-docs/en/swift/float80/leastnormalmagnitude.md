---
title: leastNormalMagnitude
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/leastnormalmagnitude
source_url: 'https://developer.apple.com/documentation/swift/float80/leastnormalmagnitude'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/leastnormalmagnitude.json'
content_hash: 'sha256:1f3d439b7af53990'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# leastNormalMagnitude

<sub>Type Property</sub>

The least positive normal number.

<sub>macOS</sub>

```swift
static var leastNormalMagnitude: Float80 { get }
```

## Discussion

This value compares less than or equal to all positive normal numbers. There may be smaller positive numbers, but they are _subnormal_, meaning that they are represented with less precision than normal numbers.

This value corresponds to type-specific C macros such as `FLT_MIN` and `DBL_MIN`. The naming of those macros is slightly misleading, because subnormals, zeros, and negative numbers are smaller than this value.
