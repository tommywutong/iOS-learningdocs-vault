---
title: bitWidth
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/uint128/bitwidth
source_url: 'https://developer.apple.com/documentation/swift/uint128/bitwidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint128/bitwidth.json'
content_hash: 'sha256:a0dedb1a5c630aa2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt128](../uint128.md)

# bitWidth

<sub>Type Property</sub>

The number of bits used for the underlying binary representation of values of this type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var bitWidth: Int { get }
```

## Discussion

An unsigned, fixed-width integer type can represent values from 0 through `(2 ** bitWidth) - 1`, where `**` is exponentiation. A signed, fixed-width integer type can represent values from `-(2 ** (bitWidth - 1))` through `(2 ** (bitWidth - 1)) - 1`. For example, the `Int8` type has a `bitWidth` value of 8 and can store any integer in the range `-128...127`.
