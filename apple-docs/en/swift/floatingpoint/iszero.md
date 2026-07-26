---
title: isZero
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpoint/iszero
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/iszero'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/iszero.json'
content_hash: 'sha256:24566d07a5062f92'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

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
