---
title: isASCIIHexDigit
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/isasciihexdigit
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/isasciihexdigit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/isasciihexdigit.json'
content_hash: 'sha256:8a555414c8d46cee'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# isASCIIHexDigit

<sub>Instance Property</sub>

A Boolean value indicating whether the scalar is an ASCII character commonly used for the representation of hexadecimal numbers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isASCIIHexDigit: Bool { get }
```

## Discussion

The only scalars for which this property is `true` are:

- U+0030…U+0039: DIGIT ZERO…DIGIT NINE
- U+0041…U+0046: LATIN CAPITAL LETTER A…LATIN CAPITAL LETTER F
- U+0061…U+0066: LATIN SMALL LETTER A…LATIN SMALL LETTER F

This property corresponds to the “ASCII_Hex_Digit” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).
