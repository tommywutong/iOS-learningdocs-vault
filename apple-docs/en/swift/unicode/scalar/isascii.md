---
title: isASCII
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/isascii
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/isascii'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/isascii.json'
content_hash: 'sha256:3afc468f3acc3003'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Unicode](../../unicode.md) · [Scalar](../scalar.md)

# isASCII

<sub>Instance Property</sub>

A Boolean value indicating whether the Unicode scalar is an ASCII character.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isASCII: Bool { get }
```

## Discussion

ASCII characters have a scalar value between 0 and 127, inclusive. For example:

```swift
let canyon = "Cañón"
for scalar in canyon.unicodeScalars {
    print(scalar, scalar.isASCII, scalar.value)
}
// Prints "C true 67"
// Prints "a true 97"
// Prints "ñ false 241"
// Prints "ó false 243"
// Prints "n true 110"
```

## See Also

### Inspecting a Scalar

- [value](value.md) — A numeric representation of the Unicode scalar.
- [properties](properties-swift.property.md) — Properties of this scalar defined by the Unicode standard.
- [Properties](properties-swift.struct.md) — A value that provides access to properties of a Unicode scalar that are defined by the Unicode standard.
- [hash(into:)](<hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.
