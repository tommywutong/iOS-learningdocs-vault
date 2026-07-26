---
title: isIDSBinaryOperator
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/isidsbinaryoperator
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/isidsbinaryoperator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/isidsbinaryoperator.json'
content_hash: 'sha256:7187c7858a8ca6b8'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# isIDSBinaryOperator

<sub>Instance Property</sub>

A Boolean value indicating whether the scalar is an ideographic description character that determines how the two ideographic characters or ideographic description sequences that follow it are to be combined to form a single character.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isIDSBinaryOperator: Bool { get }
```

## Discussion

Ideographic description characters are technically printable characters, but advanced rendering engines may use them to approximate ideographs that are otherwise unrepresentable.

This property corresponds to the “IDS_Binary_Operator” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).
