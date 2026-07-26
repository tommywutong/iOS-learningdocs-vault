---
title: isZero
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float16/iszero
source_url: 'https://developer.apple.com/documentation/swift/float16/iszero'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/iszero.json'
content_hash: 'sha256:34c5834130ec95b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# isZero

<sub>Instance Property</sub>

A Boolean value indicating whether the instance is equal to zero.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

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
