---
title: isXIDStart
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/isxidstart
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/isxidstart'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/isxidstart.json'
content_hash: 'sha256:83380e7306abab24'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# isXIDStart

<sub>Instance Property</sub>

A Boolean value indicating whether the scalar is one which is recommended to be allowed to appear in a starting position in a programming language identifier, with adjustments made for NFKC normalized form.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isXIDStart: Bool { get }
```

## Discussion

The set of scalars `[:XID_Start:]` closes the set `[:ID_Start:]` under NFKC normalization by removing any scalars whose normalized form is not of the form `[:ID_Start:] [:ID_Continue:]*`.

This property corresponds to the “XID_Start” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).
