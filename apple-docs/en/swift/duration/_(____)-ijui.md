---
title: '<(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/duration/_(_:_:)-ijui'
source_url: 'https://developer.apple.com/documentation/swift/duration/_(_:_:)-ijui'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/_%28_%3A_%3A%29-ijui.json'
content_hash: 'sha256:a7774828fc3c4ed9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Duration](../duration.md)

# \<(_:_:)

<sub>Operator</sub>

Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func < (lhs: Duration, rhs: Duration) -> Bool
```

## Parameters

- `lhs` — A value to compare.

- `rhs` — Another value to compare.

## Discussion

This function is the only requirement of the `Comparable` protocol. The remainder of the relational operator functions are implemented by the standard library for any type that conforms to `Comparable`.
