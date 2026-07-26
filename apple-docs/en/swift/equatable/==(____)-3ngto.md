---
title: '==(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/equatable/==(_:_:)-3ngto'
source_url: 'https://developer.apple.com/documentation/swift/equatable/==(_:_:)-3ngto'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/equatable/%3D%3D%28_%3A_%3A%29-3ngto.json'
content_hash: 'sha256:a81562bd9b6e6092'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Equatable](../equatable.md)

# ==(_:_:)

<sub>Operator</sub>

Returns a Boolean value indicating whether two values are equal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func == (lhs: Self, rhs: Self) -> Bool
```

## Parameters

- `lhs` — A value to compare.

- `rhs` — Another value to compare.

## Discussion

Equality is the inverse of inequality. For any values `a` and `b`, `a == b` implies that `a != b` is `false`.
