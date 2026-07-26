---
title: trailingZeroBitCount
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int128/trailingzerobitcount
source_url: 'https://developer.apple.com/documentation/swift/int128/trailingzerobitcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int128/trailingzerobitcount.json'
content_hash: 'sha256:f3f00e95b7d8ce07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int128](../int128.md)

# trailingZeroBitCount

<sub>Instance Property</sub>

The number of trailing zeros in this value’s binary representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var trailingZeroBitCount: Int { get }
```

## Discussion

For example, in a fixed-width integer type with a `bitWidth` value of 8, the number -8 has three trailing zeros.

```swift
let x = Int8(bitPattern: 0b1111_1000)
// x == -8
// x.trailingZeroBitCount == 3
```

If the value is zero, then `trailingZeroBitCount` is equal to `bitWidth`.
