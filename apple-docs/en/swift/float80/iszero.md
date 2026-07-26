---
title: isZero
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/iszero
source_url: 'https://developer.apple.com/documentation/swift/float80/iszero'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/iszero.json'
content_hash: 'sha256:27ff8261201342e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# isZero

<sub>Instance Property</sub>

A Boolean value indicating whether the instance is equal to zero.

<sub>macOS</sub>

```swift
var isZero: Bool { get }
```

## Discussion

The `isZero` property of a value `x` is `true` when `x` represents either `-0.0` or `+0.0`. `x.isZero` is equivalent to the following comparison: `x == 0.0`.

```swift
let x = -0.0
x.isZero        // true
x == 0.0        // true
```
