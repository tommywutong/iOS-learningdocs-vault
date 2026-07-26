---
title: isEmojiPresentation
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.2+, iPadOS 10.2+, Mac Catalyst 10.2+, macOS 10.12.2+, tvOS 10.1+, visionOS 1.0+, watchOS 3.1.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/isemojipresentation
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/isemojipresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/isemojipresentation.json'
content_hash: 'sha256:6951044aba43777f'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# isEmojiPresentation

<sub>Instance Property</sub>

A Boolean value indicating whether the scalar is one that should be rendered with an emoji presentation, rather than a text presentation, by default.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isEmojiPresentation: Bool { get }
```

## Discussion

Scalars that have default to emoji presentation can be followed by U+FE0E VARIATION SELECTOR-15 to request the text presentation of the scalar instead. Likewise, scalars that default to text presentation can be followed by U+FE0F VARIATION SELECTOR-16 to request the emoji presentation.

This property corresponds to the “Emoji_Presentation” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).
