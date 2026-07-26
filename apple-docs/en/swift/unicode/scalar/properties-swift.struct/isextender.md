---
title: isExtender
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/isextender
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/isextender'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/isextender.json'
content_hash: 'sha256:9c5ec7ddbb94dab5'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# isExtender

<sub>Instance Property</sub>

A Boolean value indicating whether the scalar’s principal function is to extend the value or shape of a preceding alphabetic scalar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isExtender: Bool { get }
```

## Discussion

Typical extenders are length and iteration marks.

This property corresponds to the “Extender” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).
