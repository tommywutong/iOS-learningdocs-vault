---
title: titlecaseMapping
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/titlecasemapping
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/titlecasemapping'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/titlecasemapping.json'
content_hash: 'sha256:67c84b138b1a0620'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# titlecaseMapping

<sub>Instance Property</sub>

The titlecase mapping of the scalar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var titlecaseMapping: String { get }
```

## Discussion

This property is a `String`, not a `Unicode.Scalar` or `Character`, because some mappings may transform a scalar into multiple scalars or graphemes. For example, the ligature “ﬁ” (U+FB01 LATIN SMALL LIGATURE FI) becomes “Fi” (U+0046 LATIN CAPITAL LETTER F, U+0069 LATIN SMALL LETTER I) when converted to titlecase.

This property corresponds to the “Titlecase_Mapping” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).
