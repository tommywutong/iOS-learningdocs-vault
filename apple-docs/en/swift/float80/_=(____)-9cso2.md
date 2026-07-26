---
title: '<=(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float80/_=(_:_:)-9cso2'
source_url: 'https://developer.apple.com/documentation/swift/float80/_=(_:_:)-9cso2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/_%3D%28_%3A_%3A%29-9cso2.json'
content_hash: 'sha256:4bad6d549be79d2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# \<=(_:_:)

<sub>Operator</sub>

Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.

<sub>macOS</sub>

```swift
static func <= (lhs: borrowing Self, rhs: borrowing Self) -> Bool
```

## Parameters

- `lhs` — A value to compare.

- `rhs` — Another value to compare.

## Discussion

This is the default implementation of the less-than-or-equal-to operator (`<=`) for any type that conforms to `Comparable`.
