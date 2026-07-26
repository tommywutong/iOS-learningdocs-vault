---
title: uppercaseMapping
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/uppercasemapping
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/uppercasemapping'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/uppercasemapping.json'
content_hash: 'sha256:5ecdb793d9caefd2'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# uppercaseMapping

<sub>Instance Property</sub>

The uppercase mapping of the scalar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var uppercaseMapping: String { get }
```

## Discussion

This property is a `String`, not a `Unicode.Scalar` or `Character`, because some mappings may transform a scalar into multiple scalars or graphemes. For example, the German letter “ß” (U+00DF LATIN SMALL LETTER SHARP S) becomes “SS” (U+0053 LATIN CAPITAL LETTER S, U+0053 LATIN CAPITAL LETTER S) when converted to uppercase.

This property corresponds to the “Uppercase_Mapping” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).
