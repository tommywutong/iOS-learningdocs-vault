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
doc_path: '/documentation/swift/comparable/_=(_:_:)-6cgpr'
source_url: 'https://developer.apple.com/documentation/swift/comparable/_=(_:_:)-6cgpr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/comparable/_%3D%28_%3A_%3A%29-6cgpr.json'
content_hash: 'sha256:8186977040f239c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Comparable](../comparable.md)

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
