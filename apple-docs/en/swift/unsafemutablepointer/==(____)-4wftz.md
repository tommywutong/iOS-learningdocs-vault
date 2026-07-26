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
doc_path: '/documentation/swift/unsafemutablepointer/==(_:_:)-4wftz'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablepointer/==(_:_:)-4wftz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablepointer/%3D%3D%28_%3A_%3A%29-4wftz.json'
content_hash: 'sha256:393fa4668c681d91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutablePointer](../unsafemutablepointer.md)

# ==(_:_:)

<sub>Operator</sub>

Returns a Boolean value indicating whether two values are equal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func == (x: Self, y: Self) -> Bool
```

## Discussion

Equality is the inverse of inequality. For any values `a` and `b`, `a == b` implies that `a != b` is `false`.
