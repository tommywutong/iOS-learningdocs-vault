---
title: isIDStart
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/isidstart
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/isidstart'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/isidstart.json'
content_hash: 'sha256:4880feb8ceb3d154'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# isIDStart

<sub>Instance Property</sub>

A Boolean value indicating whether the scalar is one which is recommended to be allowed to appear in a starting position in a programming language identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isIDStart: Bool { get }
```

## Discussion

Applications that store identifiers in NFKC normalized form should instead use `isXIDStart` to check whether a scalar is a valid identifier character.

This property corresponds to the “ID_Start” and the “Other_ID_Start” properties in the [Unicode Standard](http://www.unicode.org/versions/latest/).
