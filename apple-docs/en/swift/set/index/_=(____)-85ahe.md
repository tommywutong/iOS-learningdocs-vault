---
title: '>=(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/set/index/_=(_:_:)-85ahe'
source_url: 'https://developer.apple.com/documentation/swift/set/index/_=(_:_:)-85ahe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/index/_%3D%28_%3A_%3A%29-85ahe.json'
content_hash: 'sha256:2c6d2fb2914eb523'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Set](../../set.md) · [Index](../index.md)

# \>=(_:_:)

<sub>Operator</sub>

Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func >= (lhs: borrowing Self, rhs: borrowing Self) -> Bool
```

## Parameters

- `lhs` — A value to compare.

- `rhs` — Another value to compare.

## Return Value

`true` if `lhs` is greater than or equal to `rhs`; otherwise, `false`.

## Discussion

This is the default implementation of the greater-than-or-equal-to operator (`>=`) for any type that conforms to `Comparable`.
