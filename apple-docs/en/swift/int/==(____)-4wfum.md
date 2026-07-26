---
title: '==(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int/==(_:_:)-4wfum'
source_url: 'https://developer.apple.com/documentation/swift/int/==(_:_:)-4wfum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int/%3D%3D%28_%3A_%3A%29-4wfum.json'
content_hash: 'sha256:e0006ff864b7eaf5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int](../int.md)

# ==(_:_:)

<sub>Operator</sub>

Returns a Boolean value indicating whether two values are equal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func == (x: Self, y: Self) -> Bool
```

## Discussion

Equality is the inverse of inequality. For any values `a` and `b`, `a == b` implies that `a != b` is `false`.
