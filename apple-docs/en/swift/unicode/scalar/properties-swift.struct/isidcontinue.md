---
title: isIDContinue
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/isidcontinue
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/isidcontinue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/isidcontinue.json'
content_hash: 'sha256:108bbc0ed69771cc'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# isIDContinue

<sub>Instance Property</sub>

A Boolean value indicating whether the scalar is one which is recommended to be allowed to appear in a non-starting position in a programming language identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isIDContinue: Bool { get }
```

## Discussion

Applications that store identifiers in NFKC normalized form should instead use `isXIDContinue` to check whether a scalar is a valid identifier character.

This property corresponds to the “ID_Continue” and the “Other_ID_Continue” properties in the [Unicode Standard](http://www.unicode.org/versions/latest/).
