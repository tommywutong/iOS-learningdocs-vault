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
doc_path: '/documentation/swift/never/_=(_:_:)-7u3hd'
source_url: 'https://developer.apple.com/documentation/swift/never/_=(_:_:)-7u3hd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/never/_%3D%28_%3A_%3A%29-7u3hd.json'
content_hash: 'sha256:005d876b58f281b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Never](../never.md)

# \<=(_:_:)

<sub>Operator</sub>

Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func <= (lhs: borrowing Self, rhs: borrowing Self) -> Bool
```

## Parameters

- `lhs` — A value to compare.

- `rhs` — Another value to compare.

## Discussion

This is the default implementation of the less-than-or-equal-to operator (`<=`) for any type that conforms to `Comparable`.
