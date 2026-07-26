---
title: name
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/name
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/name.json'
content_hash: 'sha256:a86ccf4235ff6936'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# name

<sub>Instance Property</sub>

The published name of the scalar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var name: String? { get }
```

## Discussion

Some scalars, such as control characters, do not have a value for this property in the Unicode Character Database. For such scalars, this property is `nil`.

This property corresponds to the “Name” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).
