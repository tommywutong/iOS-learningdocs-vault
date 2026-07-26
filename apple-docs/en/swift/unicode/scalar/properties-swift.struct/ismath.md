---
title: isMath
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/ismath
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/ismath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/ismath.json'
content_hash: 'sha256:dcdb3ed39c79f5f1'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# isMath

<sub>Instance Property</sub>

A Boolean value indicating whether the scalar is one that naturally appears in mathematical contexts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isMath: Bool { get }
```

## Discussion

The set of scalars for which this property is `true` includes mathematical operators and symbols as well as specific Greek and Hebrew letter variants that are categorized as symbols. Notably, it does _not_ contain the standard digits or Latin/Greek letter blocks; instead, it contains the mathematical Latin, Greek, and Arabic letters and numbers defined in the Supplemental Multilingual Plane.

This property corresponds to the “Math” and the “Other_Math” properties in the [Unicode Standard](http://www.unicode.org/versions/latest/).
