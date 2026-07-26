---
title: '%(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/binaryinteger/_(_:_:)-30ngi'
source_url: 'https://developer.apple.com/documentation/swift/binaryinteger/_(_:_:)-30ngi'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/binaryinteger/_%28_%3A_%3A%29-30ngi.json'
content_hash: 'sha256:84c4ade66f7f8048'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BinaryInteger](../binaryinteger.md)

# %(_:_:)

<sub>Operator</sub>

Returns the remainder of dividing the first value by the second.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func % (lhs: Self, rhs: Self) -> Self
```

## Parameters

- `lhs` — The value to divide.

- `rhs` — The value to divide `lhs` by. `rhs` must not be zero.

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
