---
title: '/(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int/_(_:_:)-7j9bj'
source_url: 'https://developer.apple.com/documentation/swift/int/_(_:_:)-7j9bj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int/_%28_%3A_%3A%29-7j9bj.json'
content_hash: 'sha256:55522afd50ec79ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int](../int.md)

# /(_:_:)

<sub>Operator</sub>

Returns the quotient of dividing the first value by the second.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func / (lhs: Int, rhs: Int) -> Int
```

## Parameters

- `lhs` — The value to divide.

- `rhs` — The value to divide `lhs` by. `rhs` must not be zero.

## Discussion

For integer types, any remainder of the division is discarded.

```swift
let x = 21 / 5
// x == 4
```
