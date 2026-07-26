---
title: '<(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float80/_(_:_:)-3kkyi'
source_url: 'https://developer.apple.com/documentation/swift/float80/_(_:_:)-3kkyi'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/_%28_%3A_%3A%29-3kkyi.json'
content_hash: 'sha256:8266602846447187'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# \<(_:_:)

<sub>Operator</sub>

Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.

<sub>macOS</sub>

```swift
static func < (lhs: Self, rhs: Self) -> Bool
```

## Parameters

- `lhs` — A value to compare.

- `rhs` — Another value to compare.

## Discussion

This function is the only requirement of the `Comparable` protocol. The remainder of the relational operator functions are implemented by the standard library for any type that conforms to `Comparable`.
