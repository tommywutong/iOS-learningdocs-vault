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
doc_path: '/documentation/swift/int64/_(_:_:)-2xs3w'
source_url: 'https://developer.apple.com/documentation/swift/int64/_(_:_:)-2xs3w'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int64/_%28_%3A_%3A%29-2xs3w.json'
content_hash: 'sha256:0731ee6694e95a71'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int64](../int64.md)

# %(_:_:)

<sub>Operator</sub>

Returns the remainder of dividing the first value by the second.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func % (lhs: Int64, rhs: Int64) -> Int64
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
