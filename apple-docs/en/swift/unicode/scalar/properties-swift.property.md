---
title: properties
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.property
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.property.json'
content_hash: 'sha256:82962dc71ee3ed3b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Unicode](../../unicode.md) · [Scalar](../scalar.md)

# properties

<sub>Instance Property</sub>

Properties of this scalar defined by the Unicode standard.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var properties: Unicode.Scalar.Properties { get }
```

## Discussion

Use this property to access the Unicode properties of a Unicode scalar value. The following code tests whether a string contains any math symbols:

```swift
let question = "Which is larger, 3 * 3 * 3 or 10 + 10 + 10?"
let hasMathSymbols = question.unicodeScalars.contains(where: {
    $0.properties.isMath
})
// hasMathSymbols == true
```

## See Also

### Inspecting a Scalar

- [value](value.md) — A numeric representation of the Unicode scalar.
- [Properties](properties-swift.struct.md) — A value that provides access to properties of a Unicode scalar that are defined by the Unicode standard.
- [hash(into:)](<hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.
- [isASCII](isascii.md) — A Boolean value indicating whether the Unicode scalar is an ASCII character.
