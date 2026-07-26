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
doc_path: '/documentation/swift/uint64/_=(_:_:)-9jhbb'
source_url: 'https://developer.apple.com/documentation/swift/uint64/_=(_:_:)-9jhbb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint64/_%3D%28_%3A_%3A%29-9jhbb.json'
content_hash: 'sha256:4c2a8ec4b8cc6546'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt64](../uint64.md)

# /=(_:_:)

<sub>Operator</sub>

Divides the first value by the second and stores the quotient in the left-hand-side variable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func /= (lhs: inout UInt64, rhs: UInt64)
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
