---
title: '!=(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint128/!=(_:_:)-68qot'
source_url: 'https://developer.apple.com/documentation/swift/uint128/!=(_:_:)-68qot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint128/%21%3D%28_%3A_%3A%29-68qot.json'
content_hash: 'sha256:d1c458d12c94ea2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt128](../uint128.md)

# !=(_:_:)

<sub>Operator</sub>

Returns a Boolean value indicating whether two values are not equal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func != (lhs: Self, rhs: Self) -> Bool
```

## Parameters

- `lhs` — A value to compare.

- `rhs` — Another value to compare.

## Discussion

Inequality is the inverse of equality. For any values `a` and `b`, `a != b` implies that `a == b` is `false`.

This is the default implementation of the not-equal-to operator (`!=`) for any type that conforms to `Equatable`.
