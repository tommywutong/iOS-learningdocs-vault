---
title: words
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int/words-swift.property
source_url: 'https://developer.apple.com/documentation/swift/int/words-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int/words-swift.property.json'
content_hash: 'sha256:83667e0249921c22'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int](../int.md)

# words

<sub>Instance Property</sub>

A collection containing the words of this value’s binary representation, in order from the least significant to most significant.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var words: Int.Words { get }
```

## Discussion

Negative values are returned in two’s complement representation, regardless of the type’s underlying implementation.

## See Also

### Working with Binary Representation

- [bitWidth](bitwidth.md) — The number of bits used for the underlying binary representation of values of this type.
- [bitWidth](bitwidth-swift.property.md) — The number of bits in the current binary representation of this value.
- [nonzeroBitCount](nonzerobitcount.md) — The number of bits equal to 1 in this value’s binary representation.
- [leadingZeroBitCount](leadingzerobitcount.md) — The number of leading zeros in this value’s binary representation.
- [trailingZeroBitCount](trailingzerobitcount.md) — The number of trailing zeros in this value’s binary representation.
- [Words](words-swift.struct.md) — A type that represents the words of this integer.
