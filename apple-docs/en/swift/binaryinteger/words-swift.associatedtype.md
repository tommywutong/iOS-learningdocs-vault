---
title: Words
framework: Swift
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/binaryinteger/words-swift.associatedtype
source_url: 'https://developer.apple.com/documentation/swift/binaryinteger/words-swift.associatedtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/binaryinteger/words-swift.associatedtype.json'
content_hash: 'sha256:0c6c431f77cfdf66'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BinaryInteger](../binaryinteger.md)

# Words

<sub>Associated Type</sub>

A type that represents the words of a binary integer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype Words : RandomAccessCollection where Self.Words.Element == UInt, Self.Words.Index == Int
```

## Discussion

The `Words` type must conform to the `RandomAccessCollection` protocol with an `Element` type of `UInt` and `Index` type of `Int`.

## See Also

### Working with Binary Representation

- [bitWidth](bitwidth.md) — The number of bits in the current binary representation of this value.
- [trailingZeroBitCount](trailingzerobitcount.md) — The number of trailing zeros in this value’s binary representation.
- [words](words-swift.property.md) — A collection containing the words of this value’s binary representation, in order from the least significant to most significant.
