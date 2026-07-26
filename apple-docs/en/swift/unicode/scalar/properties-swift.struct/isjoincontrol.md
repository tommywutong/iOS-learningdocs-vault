---
title: isJoinControl
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/isjoincontrol
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/isjoincontrol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/isjoincontrol.json'
content_hash: 'sha256:a5febab60a8e39f0'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# isJoinControl

<sub>Instance Property</sub>

A Boolean value indicating whether the scalar is a format control character that has a specific function in controlling cursive joining and ligation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isJoinControl: Bool { get }
```

## Discussion

There are two scalars for which this property is `true`:

- When U+200C ZERO WIDTH NON-JOINER is inserted between two characters, it directs the rendering engine to render them separately/disconnected when it might otherwise render them as a ligature. For example, a rendering engine might display “fl” in English as a connected glyph; inserting the zero width non-joiner would force them to be rendered as disconnected glyphs.
- When U+200D ZERO WIDTH JOINER is inserted between two characters, it directs the rendering engine to render them as a connected glyph when it would otherwise render them independently. The zero width joiner is also used to construct complex emoji from sequences of base emoji characters. For example, the various “family” emoji are encoded as sequences of man, woman, or child emoji that are interleaved with zero width joiners.

This property corresponds to the “Join_Control” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).
