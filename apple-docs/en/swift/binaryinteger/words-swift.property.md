---
title: words
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/binaryinteger/words-swift.property
source_url: 'https://developer.apple.com/documentation/swift/binaryinteger/words-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/binaryinteger/words-swift.property.json'
content_hash: 'sha256:21b5d0c5fbe39014'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BinaryInteger](../binaryinteger.md)

# words

<sub>Instance Property</sub>

A collection containing the words of this value’s binary representation, in order from the least significant to most significant.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var words: Self.Words { get }
```

## Discussion

Negative values are returned in two’s complement representation, regardless of the type’s underlying implementation.

## See Also

### Working with Binary Representation

- [bitWidth](bitwidth.md) — The number of bits in the current binary representation of this value.
- [trailingZeroBitCount](trailingzerobitcount.md) — The number of trailing zeros in this value’s binary representation.
- [Words](words-swift.associatedtype.md) — A type that represents the words of a binary integer.
