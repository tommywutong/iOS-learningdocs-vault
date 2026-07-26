---
title: '/=(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int16/_=(_:_:)-15qjk'
source_url: 'https://developer.apple.com/documentation/swift/int16/_=(_:_:)-15qjk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int16/_%3D%28_%3A_%3A%29-15qjk.json'
content_hash: 'sha256:535ab7af2d3e96aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int16](../int16.md)

# /=(_:_:)

<sub>Operator</sub>

Divides the first value by the second and stores the quotient in the left-hand-side variable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func /= (lhs: inout Int16, rhs: Int16)
```

## Parameters

- `lhs` — The value to divide.

- `rhs` — The value to divide `lhs` by. `rhs` must not be zero.

## Discussion

For integer types, any remainder of the division is discarded.

```swift
var x = 21
x /= 5
// x == 4
```
