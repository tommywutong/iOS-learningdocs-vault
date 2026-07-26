---
title: bitWidth
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int/bitwidth-swift.property
source_url: 'https://developer.apple.com/documentation/swift/int/bitwidth-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int/bitwidth-swift.property.json'
content_hash: 'sha256:86e7f0856d3ef936'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int](../int.md)

# bitWidth

<sub>Instance Property</sub>

The number of bits in the current binary representation of this value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var bitWidth: Int { get }
```

## Discussion

This property is a constant for instances of fixed-width integer types.

## See Also

### Working with Binary Representation

- [bitWidth](bitwidth.md) — The number of bits used for the underlying binary representation of values of this type.
- [nonzeroBitCount](nonzerobitcount.md) — The number of bits equal to 1 in this value’s binary representation.
- [leadingZeroBitCount](leadingzerobitcount.md) — The number of leading zeros in this value’s binary representation.
- [trailingZeroBitCount](trailingzerobitcount.md) — The number of trailing zeros in this value’s binary representation.
- [words](words-swift.property.md) — A collection containing the words of this value’s binary representation, in order from the least significant to most significant.
- [Words](words-swift.struct.md) — A type that represents the words of this integer.
