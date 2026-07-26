---
title: '^=(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int128/_=(_:_:)-ckwk'
source_url: 'https://developer.apple.com/documentation/swift/int128/_=(_:_:)-ckwk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int128/_%3D%28_%3A_%3A%29-ckwk.json'
content_hash: 'sha256:2eec0e19620c8173'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int128](../int128.md)

# ^=(_:_:)

<sub>Operator</sub>

Stores the result of performing a bitwise XOR operation on the two given values in the left-hand-side variable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func ^= (a: inout Int128, b: Int128)
```

## Discussion

A bitwise XOR operation, also known as an exclusive OR operation, results in a value that has each bit set to `1` where _one or the other but not both_ of its arguments had that bit set to `1`. For example:

```swift
var x: UInt8 = 5          // 0b00000101
let y: UInt8 = 14         // 0b00001110
x ^= y                    // 0b00001011
```
