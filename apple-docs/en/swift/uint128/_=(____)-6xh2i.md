---
title: '/=(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint128/_=(_:_:)-6xh2i'
source_url: 'https://developer.apple.com/documentation/swift/uint128/_=(_:_:)-6xh2i'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint128/_%3D%28_%3A_%3A%29-6xh2i.json'
content_hash: 'sha256:5fcfaba394859dc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt128](../uint128.md)

# /=(_:_:)

<sub>Operator</sub>

Divides the first value by the second and stores the quotient in the left-hand-side variable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func /= (a: inout UInt128, b: UInt128)
```

## Discussion

For integer types, any remainder of the division is discarded.

```swift
var x = 21
x /= 5
// x == 4
```
