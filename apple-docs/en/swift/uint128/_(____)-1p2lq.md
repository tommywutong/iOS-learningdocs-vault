---
title: '<(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint128/_(_:_:)-1p2lq'
source_url: 'https://developer.apple.com/documentation/swift/uint128/_(_:_:)-1p2lq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint128/_%28_%3A_%3A%29-1p2lq.json'
content_hash: 'sha256:825db6554fefe3e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt128](../uint128.md)

# \<(_:_:)

<sub>Operator</sub>

Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func < (a: UInt128, b: UInt128) -> Bool
```

## Discussion

This function is the only requirement of the `Comparable` protocol. The remainder of the relational operator functions are implemented by the standard library for any type that conforms to `Comparable`.
