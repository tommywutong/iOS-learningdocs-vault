---
title: '<(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int64/_(_:_:)-15gfv'
source_url: 'https://developer.apple.com/documentation/swift/int64/_(_:_:)-15gfv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int64/_%28_%3A_%3A%29-15gfv.json'
content_hash: 'sha256:bddce41f6d34329d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int64](../int64.md)

# \<(_:_:)

<sub>Operator</sub>

Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func < (lhs: Int64, rhs: Int64) -> Bool
```

## Parameters

- `lhs` — A value to compare.

- `rhs` — Another value to compare.

## Discussion

This function is the only requirement of the `Comparable` protocol. The remainder of the relational operator functions are implemented by the standard library for any type that conforms to `Comparable`.
