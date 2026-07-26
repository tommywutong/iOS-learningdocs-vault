---
title: '|=(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int16/_=(_:_:)-9yk6s'
source_url: 'https://developer.apple.com/documentation/swift/int16/_=(_:_:)-9yk6s'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int16/_%3D%28_%3A_%3A%29-9yk6s.json'
content_hash: 'sha256:ebcb1f44c286f062'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int16](../int16.md)

# |=(_:_:)

<sub>Operator</sub>

Stores the result of performing a bitwise OR operation on the two given values in the left-hand-side variable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func |= (lhs: inout Int16, rhs: Int16)
```

## Parameters

- `lhs` — An integer value.

- `rhs` — Another integer value.

## Discussion

A bitwise OR operation results in a value that has each bit set to `1` where _one or both_ of its arguments have that bit set to `1`. For example:

```swift
var x: UInt8 = 5          // 0b00000101
let y: UInt8 = 14         // 0b00001110
x |= y                    // 0b00001111
```
