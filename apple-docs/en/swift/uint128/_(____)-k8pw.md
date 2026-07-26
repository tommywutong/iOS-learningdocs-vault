---
title: '|(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint128/_(_:_:)-k8pw'
source_url: 'https://developer.apple.com/documentation/swift/uint128/_(_:_:)-k8pw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint128/_%28_%3A_%3A%29-k8pw.json'
content_hash: 'sha256:d725b8ac33931e58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt128](../uint128.md)

# |(_:_:)

<sub>Operator</sub>

Returns the result of performing a bitwise OR operation on the two given values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func | (lhs: Self, rhs: Self) -> Self
```

## Parameters

- `lhs` — An integer value.

- `rhs` — Another integer value.

## Discussion

A bitwise OR operation results in a value that has each bit set to `1` where _one or both_ of its arguments have that bit set to `1`. For example:

```swift
let x: UInt8 = 5          // 0b00000101
let y: UInt8 = 14         // 0b00001110
let z = x | y             // 0b00001111
// z == 15
```
