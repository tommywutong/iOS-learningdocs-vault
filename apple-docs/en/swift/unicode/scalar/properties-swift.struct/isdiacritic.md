---
title: isDiacritic
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/isdiacritic
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/isdiacritic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/isdiacritic.json'
content_hash: 'sha256:92aad82a7fd327e5'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# isDiacritic

<sub>Instance Property</sub>

A Boolean value indicating whether the scalar is a diacritic.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isDiacritic: Bool { get }
```

## Discussion

Diacritics are scalars that linguistically modify the meaning of another scalar to which they apply. Scalars for which this property is `true` are frequently, but not always, combining marks or modifiers.

This property corresponds to the “Diacritic” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).
