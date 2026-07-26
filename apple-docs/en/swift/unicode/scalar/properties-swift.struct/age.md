---
title: age
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/age
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/age'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/age.json'
content_hash: 'sha256:0ce45b5caa0a25f8'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# age

<sub>Instance Property</sub>

The earliest version of the Unicode Standard in which the scalar was assigned.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var age: Unicode.Version? { get }
```

## Discussion

This value is `nil` for code points that have not yet been assigned.

This property corresponds to the “Age” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).
