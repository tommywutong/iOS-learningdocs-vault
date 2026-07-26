---
title: '^(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint32/_(_:_:)-9mox3'
source_url: 'https://developer.apple.com/documentation/swift/uint32/_(_:_:)-9mox3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint32/_%28_%3A_%3A%29-9mox3.json'
content_hash: 'sha256:ee2e904b13bd1950'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt32](../uint32.md)

# ^(_:_:)

<sub>Operator</sub>

Returns the result of performing a bitwise XOR operation on the two given values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func ^ (lhs: UInt32, rhs: UInt32) -> UInt32
```

## Parameters

- `lhs` — An integer value.

- `rhs` — Another integer value.

## Discussion

A bitwise XOR operation, also known as an exclusive OR operation, results in a value that has each bit set to `1` where _one or the other but not both_ of its arguments had that bit set to `1`. For example:

```swift
let x: UInt8 = 5          // 0b00000101
let y: UInt8 = 14         // 0b00001110
let z = x ^ y             // 0b00001011
// z == 11
```
