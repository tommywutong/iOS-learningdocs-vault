---
title: '%(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint128/_(_:_:)-3t4ck'
source_url: 'https://developer.apple.com/documentation/swift/uint128/_(_:_:)-3t4ck'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint128/_%28_%3A_%3A%29-3t4ck.json'
content_hash: 'sha256:e68227591bef4da3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt128](../uint128.md)

# %(_:_:)

<sub>Operator</sub>

Returns the remainder of dividing the first value by the second.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func % (a: UInt128, b: UInt128) -> UInt128
```

## Discussion

The result of the remainder operator (`%`) has the same sign as `lhs` and has a magnitude less than `rhs.magnitude`.

```swift
let x = 22 % 5
// x == 2
let y = 22 % -5
// y == 2
let z = -22 % -5
// z == -2
```

For any two integers `a` and `b`, their quotient `q`, and their remainder `r`, `a == b * q + r`.
