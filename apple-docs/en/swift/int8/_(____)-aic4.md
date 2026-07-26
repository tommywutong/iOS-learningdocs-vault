---
title: '/(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int8/_(_:_:)-aic4'
source_url: 'https://developer.apple.com/documentation/swift/int8/_(_:_:)-aic4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int8/_%28_%3A_%3A%29-aic4.json'
content_hash: 'sha256:23fa51a944806cc2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int8](../int8.md)

# /(_:_:)

<sub>Operator</sub>

Returns the quotient of dividing the first value by the second.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func / (lhs: Int8, rhs: Int8) -> Int8
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
