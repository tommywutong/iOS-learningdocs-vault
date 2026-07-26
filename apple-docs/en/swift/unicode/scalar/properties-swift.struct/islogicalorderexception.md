---
title: isLogicalOrderException
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/islogicalorderexception
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/islogicalorderexception'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/islogicalorderexception.json'
content_hash: 'sha256:43405500eeb5b0ac'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# isLogicalOrderException

<sub>Instance Property</sub>

A Boolean value indicating whether the scalar requires special handling for operations involving ordering, such as sorting and searching.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isLogicalOrderException: Bool { get }
```

## Discussion

This property applies to a small number of spacing vowel letters occurring in some Southeast Asian scripts like Thai and Lao, which use a visual order display model. Such letters are stored in text ahead of syllable-initial consonants.

This property corresponds to the “Logical_Order_Exception” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).
