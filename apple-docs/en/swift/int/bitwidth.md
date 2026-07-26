---
title: bitWidth
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int/bitwidth
source_url: 'https://developer.apple.com/documentation/swift/int/bitwidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int/bitwidth.json'
content_hash: 'sha256:8530bb0ae673b0e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int](../int.md)

# bitWidth

<sub>Type Property</sub>

The number of bits used for the underlying binary representation of values of this type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var bitWidth: Int { get }
```

## Discussion

The bit width of a `Int` instance is 32 on 32-bit platforms and 64 on 64-bit platforms.

## See Also

### Working with Binary Representation

- [bitWidth](bitwidth-swift.property.md) — The number of bits in the current binary representation of this value.
- [nonzeroBitCount](nonzerobitcount.md) — The number of bits equal to 1 in this value’s binary representation.
- [leadingZeroBitCount](leadingzerobitcount.md) — The number of leading zeros in this value’s binary representation.
- [trailingZeroBitCount](trailingzerobitcount.md) — The number of trailing zeros in this value’s binary representation.
- [words](words-swift.property.md) — A collection containing the words of this value’s binary representation, in order from the least significant to most significant.
- [Words](words-swift.struct.md) — A type that represents the words of this integer.
