---
title: isIdeographic
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/isideographic
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/isideographic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/isideographic.json'
content_hash: 'sha256:f53dd2354e7a6f22'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# isIdeographic

<sub>Instance Property</sub>

A Boolean value indicating whether the scalar is considered to be a CJKV (Chinese, Japanese, Korean, and Vietnamese) or other siniform (Chinese writing-related) ideograph.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isIdeographic: Bool { get }
```

## Discussion

This property roughly defines the class of “Chinese characters” and does not include characters of other logographic scripts such as Cuneiform or Egyptian Hieroglyphs.

This property corresponds to the “Ideographic” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).
