---
title: isAlphabetic
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/isalphabetic
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/isalphabetic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/isalphabetic.json'
content_hash: 'sha256:e8de14daeeb8c7b7'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# isAlphabetic

<sub>Instance Property</sub>

A Boolean value indicating whether the scalar is alphabetic.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isAlphabetic: Bool { get }
```

## Discussion

Alphabetic scalars are the primary units of alphabets and/or syllabaries.

This property corresponds to the “Alphabetic” and the “Other_Alphabetic” properties in the [Unicode Standard](http://www.unicode.org/versions/latest/).
