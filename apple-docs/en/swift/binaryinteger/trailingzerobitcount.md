---
title: trailingZeroBitCount
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/binaryinteger/trailingzerobitcount
source_url: 'https://developer.apple.com/documentation/swift/binaryinteger/trailingzerobitcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/binaryinteger/trailingzerobitcount.json'
content_hash: 'sha256:f195a5cbe414aab8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BinaryInteger](../binaryinteger.md)

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

## See Also

### Working with Binary Representation

- [bitWidth](bitwidth.md) — The number of bits in the current binary representation of this value.
- [words](words-swift.property.md) — A collection containing the words of this value’s binary representation, in order from the least significant to most significant.
- [Words](words-swift.associatedtype.md) — A type that represents the words of a binary integer.
