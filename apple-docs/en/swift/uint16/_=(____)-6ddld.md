---
title: '>=(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint16/_=(_:_:)-6ddld'
source_url: 'https://developer.apple.com/documentation/swift/uint16/_=(_:_:)-6ddld'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint16/_%3D%28_%3A_%3A%29-6ddld.json'
content_hash: 'sha256:645672a7cfd20c3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt16](../uint16.md)

# \>=(_:_:)

<sub>Operator</sub>

Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func >= <Other>(lhs: Self, rhs: Other) -> Bool where Other : BinaryInteger
```

## Parameters

- `lhs` — An integer to compare.

- `rhs` — Another integer to compare.

## Discussion

You can compare instances of any `BinaryInteger` types using the greater-than-or-equal-to operator (`>=`), even if the two instances are of different types.
