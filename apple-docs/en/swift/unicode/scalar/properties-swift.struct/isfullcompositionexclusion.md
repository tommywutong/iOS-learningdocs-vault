---
title: isFullCompositionExclusion
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/isfullcompositionexclusion
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/isfullcompositionexclusion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/isfullcompositionexclusion.json'
content_hash: 'sha256:f9acea9f8fa7e061'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# isFullCompositionExclusion

<sub>Instance Property</sub>

A Boolean value indicating whether the scalar is excluded from composition when performing Unicode normalization.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isFullCompositionExclusion: Bool { get }
```

## Discussion

This property corresponds to the “Full_Composition_Exclusion” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).
