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
doc_path: '/documentation/swift/uint64/_(_:_:)-6ykmm'
source_url: 'https://developer.apple.com/documentation/swift/uint64/_(_:_:)-6ykmm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint64/_%28_%3A_%3A%29-6ykmm.json'
content_hash: 'sha256:13e7dd76770d06dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt64](../uint64.md)

# |(_:_:)

<sub>Operator</sub>

Returns the result of performing a bitwise OR operation on the two given values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func | (lhs: UInt64, rhs: UInt64) -> UInt64
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
