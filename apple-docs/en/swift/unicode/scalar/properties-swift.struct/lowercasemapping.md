---
title: lowercaseMapping
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/lowercasemapping
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/lowercasemapping'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/lowercasemapping.json'
content_hash: 'sha256:e03dc39dc13413a2'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# lowercaseMapping

<sub>Instance Property</sub>

The lowercase mapping of the scalar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var lowercaseMapping: String { get }
```

## Discussion

This property is a `String`, not a `Unicode.Scalar` or `Character`, because some mappings may transform a scalar into multiple scalars or graphemes. For example, the character “İ” (U+0130 LATIN CAPITAL LETTER I WITH DOT ABOVE) becomes two scalars (U+0069 LATIN SMALL LETTER I, U+0307 COMBINING DOT ABOVE) when converted to lowercase.

This property corresponds to the “Lowercase_Mapping” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).
