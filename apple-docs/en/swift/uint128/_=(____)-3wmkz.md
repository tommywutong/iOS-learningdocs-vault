---
title: '<=(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint128/_=(_:_:)-3wmkz'
source_url: 'https://developer.apple.com/documentation/swift/uint128/_=(_:_:)-3wmkz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint128/_%3D%28_%3A_%3A%29-3wmkz.json'
content_hash: 'sha256:379e5b00464912a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt128](../uint128.md)

# \<=(_:_:)

<sub>Operator</sub>

Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func <= <Other>(lhs: Self, rhs: Other) -> Bool where Other : BinaryInteger
```

## Parameters

- `lhs` — An integer to compare.

- `rhs` — Another integer to compare.

## Discussion

You can compare instances of any `BinaryInteger` types using the less-than-or-equal-to operator (`<=`), even if the two instances are of different types.
