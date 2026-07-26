---
title: leadingZeroBitCount
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/fixedwidthinteger/leadingzerobitcount
source_url: 'https://developer.apple.com/documentation/swift/fixedwidthinteger/leadingzerobitcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/fixedwidthinteger/leadingzerobitcount.json'
content_hash: 'sha256:eb26e6b4e7d220dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FixedWidthInteger](../fixedwidthinteger.md)

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
