---
title: isGraphemeExtend
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/isgraphemeextend
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/isgraphemeextend'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/isgraphemeextend.json'
content_hash: 'sha256:a41f304b44c9d2f1'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# isGraphemeExtend

<sub>Instance Property</sub>

A Boolean value indicating whether the scalar is a grapheme extender.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isGraphemeExtend: Bool { get }
```

## Discussion

A grapheme extender can be thought of primarily as a non-spacing glyph that is applied above or below another glyph. For example, when the character `é` is represented in its decomposed form, the grapheme base is “e” (U+0065 LATIN SMALL LETTER E) and it is followed by a single grapheme extender, U+0301 COMBINING ACUTE ACCENT.

The set of scalars for which `isGraphemeExtend` is `true` is disjoint by definition from the set for which `isGraphemeBase` is `true`.

This property corresponds to the “Grapheme_Extend” and the “Other_Grapheme_Extend” properties in the [Unicode Standard](http://www.unicode.org/versions/latest/).
