---
title: isRadical
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/isradical
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/isradical'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/isradical.json'
content_hash: 'sha256:08c5555bb1913aae'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# isRadical

<sub>Instance Property</sub>

A Boolean value indicating whether the scalar is a radical component of CJK characters, Tangut characters, or Yi syllables.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isRadical: Bool { get }
```

## Discussion

These scalars are often the components of ideographic description sequences, as defined by the `isIDSBinaryOperator` and `isIDSTrinaryOperator` properties.

This property corresponds to the “Radical” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).
