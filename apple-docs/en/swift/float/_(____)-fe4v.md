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
doc_path: '/documentation/swift/float/_(_:_:)-fe4v'
source_url: 'https://developer.apple.com/documentation/swift/float/_(_:_:)-fe4v'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/_%28_%3A_%3A%29-fe4v.json'
content_hash: 'sha256:4afd0632b7d12f60'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

# \<(_:_:)

<sub>Operator</sub>

Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func < (x: Self, y: Self) -> Bool
```

## Discussion

This function is the only requirement of the `Comparable` protocol. The remainder of the relational operator functions are implemented by the standard library for any type that conforms to `Comparable`.
