---
title: '>(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float80/_(_:_:)-5us6c'
source_url: 'https://developer.apple.com/documentation/swift/float80/_(_:_:)-5us6c'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/_%28_%3A_%3A%29-5us6c.json'
content_hash: 'sha256:2f5e4b4448106c8a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# \>(_:_:)

<sub>Operator</sub>

Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.

<sub>macOS</sub>

```swift
static func > (lhs: borrowing Self, rhs: borrowing Self) -> Bool
```

## Parameters

- `lhs` — A value to compare.

- `rhs` — Another value to compare.

## Discussion

This is the default implementation of the greater-than operator (`>`) for any type that conforms to `Comparable`.
