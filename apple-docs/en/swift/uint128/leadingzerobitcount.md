---
title: leadingZeroBitCount
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/uint128/leadingzerobitcount
source_url: 'https://developer.apple.com/documentation/swift/uint128/leadingzerobitcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint128/leadingzerobitcount.json'
content_hash: 'sha256:5df08615a3f6bf4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt128](../uint128.md)

# leadingZeroBitCount

<sub>Instance Property</sub>

The number of leading zeros in this value’s binary representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var leadingZeroBitCount: Int { get }
```

## Discussion

For example, in a fixed-width integer type with a `bitWidth` value of 8, the number _31_ has three leading zeros.

```swift
let x: Int8 = 0b0001_1111
// x == 31
// x.leadingZeroBitCount == 3
```

If the value is zero, then `leadingZeroBitCount` is equal to `bitWidth`.
