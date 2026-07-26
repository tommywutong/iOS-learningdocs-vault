---
title: isVariationSelector
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/isvariationselector
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/isvariationselector'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/isvariationselector.json'
content_hash: 'sha256:dc62768875c43272'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# isVariationSelector

<sub>Instance Property</sub>

A Boolean value indicating whether the scalar is a variation selector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isVariationSelector: Bool { get }
```

## Discussion

Variation selectors allow rendering engines that support them to choose different glyphs to display for a particular code point.

This property corresponds to the “Variation_Selector” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).
