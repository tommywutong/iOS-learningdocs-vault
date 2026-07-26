---
title: isUnifiedIdeograph
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/isunifiedideograph
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/isunifiedideograph'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/isunifiedideograph.json'
content_hash: 'sha256:d59273669a6be062'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# isUnifiedIdeograph

<sub>Instance Property</sub>

A Boolean value indicating whether the scalar is one of the unified CJK ideographs in the Unicode Standard.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isUnifiedIdeograph: Bool { get }
```

## Discussion

This property is false for CJK punctuation and symbols, as well as for compatibility ideographs (which canonically decompose to unified ideographs).

This property corresponds to the “Unified_Ideograph” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).
