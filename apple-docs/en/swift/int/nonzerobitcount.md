---
title: nonzeroBitCount
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int/nonzerobitcount
source_url: 'https://developer.apple.com/documentation/swift/int/nonzerobitcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int/nonzerobitcount.json'
content_hash: 'sha256:280cee7042b03f83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int](../int.md)

# nonzeroBitCount

<sub>Instance Property</sub>

The number of bits equal to 1 in this value’s binary representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nonzeroBitCount: Int { get }
```

## Discussion

For example, in a fixed-width integer type with a `bitWidth` value of 8, the number _31_ has five bits equal to _1_.

```swift
let x: Int8 = 0b0001_1111
// x == 31
// x.nonzeroBitCount == 5
```

## See Also

### Working with Binary Representation

- [bitWidth](bitwidth.md) — The number of bits used for the underlying binary representation of values of this type.
- [bitWidth](bitwidth-swift.property.md) — The number of bits in the current binary representation of this value.
- [leadingZeroBitCount](leadingzerobitcount.md) — The number of leading zeros in this value’s binary representation.
- [trailingZeroBitCount](trailingzerobitcount.md) — The number of trailing zeros in this value’s binary representation.
- [words](words-swift.property.md) — A collection containing the words of this value’s binary representation, in order from the least significant to most significant.
- [Words](words-swift.struct.md) — A type that represents the words of this integer.
