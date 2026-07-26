---
title: bitWidth
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/fixedwidthinteger/bitwidth
source_url: 'https://developer.apple.com/documentation/swift/fixedwidthinteger/bitwidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/fixedwidthinteger/bitwidth.json'
content_hash: 'sha256:4cbc9992e0c94ac6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FixedWidthInteger](../fixedwidthinteger.md)

# bitWidth

<sub>Type Property</sub>

The number of bits used for the underlying binary representation of values of this type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var bitWidth: Int { get }
```

## Discussion

An unsigned, fixed-width integer type can represent values from 0 through `(2 ** bitWidth) - 1`, where `**` is exponentiation. A signed, fixed-width integer type can represent values from `-(2 ** (bitWidth - 1))` through `(2 ** (bitWidth - 1)) - 1`. For example, the `Int8` type has a `bitWidth` value of 8 and can store any integer in the range `-128...127`.

## Default Implementations

### BinaryInteger Implementations

- [bitWidth](../binaryinteger/bitwidth-57x70.md) — The number of bits in the current binary representation of this value.
