---
title: isSoftDotted
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/issoftdotted
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/issoftdotted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/issoftdotted.json'
content_hash: 'sha256:fd704af3bb80ec4c'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# isSoftDotted

<sub>Instance Property</sub>

A Boolean value indicating whether the scalar has a “soft dot” that disappears when a diacritic is placed over the scalar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isSoftDotted: Bool { get }
```

## Discussion

For example, “i” is soft dotted because the dot disappears when adding an accent mark, as in “í”.

This property corresponds to the “Soft_Dotted” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).
