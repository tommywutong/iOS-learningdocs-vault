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
doc_path: '/documentation/swift/int128/_=(_:_:)-9ag8m'
source_url: 'https://developer.apple.com/documentation/swift/int128/_=(_:_:)-9ag8m'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int128/_%3D%28_%3A_%3A%29-9ag8m.json'
content_hash: 'sha256:5711b7fed4e310fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int128](../int128.md)

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
