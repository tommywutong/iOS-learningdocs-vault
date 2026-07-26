---
title: isHexDigit
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/ishexdigit
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/ishexdigit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/ishexdigit.json'
content_hash: 'sha256:794a995a96dcf2a0'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# isHexDigit

<sub>Instance Property</sub>

A Boolean value indicating whether the scalar is one that is commonly used for the representation of hexadecimal numbers or a compatibility equivalent.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isHexDigit: Bool { get }
```

## Discussion

This property is `true` for all scalars for which `isASCIIHexDigit` is `true` as well as for their CJK halfwidth and fullwidth variants.

This property corresponds to the “Hex_Digit” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).
