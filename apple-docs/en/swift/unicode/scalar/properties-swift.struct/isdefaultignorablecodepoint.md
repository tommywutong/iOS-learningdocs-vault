---
title: isDefaultIgnorableCodePoint
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/isdefaultignorablecodepoint
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/isdefaultignorablecodepoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/isdefaultignorablecodepoint.json'
content_hash: 'sha256:52af9396ea09914a'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# isDefaultIgnorableCodePoint

<sub>Instance Property</sub>

A Boolean value indicating whether the scalar is a default-ignorable code point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isDefaultIgnorableCodePoint: Bool { get }
```

## Discussion

Default-ignorable code points are those that should be ignored by default in rendering (unless explicitly supported). They have no visible glyph or advance width in and of themselves, although they may affect the display, positioning, or adornment of adjacent or surrounding characters.

This property corresponds to the “Default_Ignorable_Code_Point” and the “Other_Default_Ignorable_Code_point” properties in the [Unicode Standard](http://www.unicode.org/versions/latest/).
