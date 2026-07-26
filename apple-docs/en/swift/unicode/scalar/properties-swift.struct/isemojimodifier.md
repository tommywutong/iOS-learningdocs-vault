---
title: isEmojiModifier
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.2+, iPadOS 10.2+, Mac Catalyst 10.2+, macOS 10.12.2+, tvOS 10.1+, visionOS 1.0+, watchOS 3.1.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/isemojimodifier
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/isemojimodifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/isemojimodifier.json'
content_hash: 'sha256:59ddfdfa80abad63'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# isEmojiModifier

<sub>Instance Property</sub>

A Boolean value indicating whether the scalar is one that can modify a base emoji that precedes it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isEmojiModifier: Bool { get }
```

## Discussion

The Fitzpatrick skin types are examples of emoji modifiers; they change the appearance of the preceding emoji base (that is, a scalar for which `isEmojiModifierBase` is true) by rendering it with a different skin tone.

This property corresponds to the “Emoji_Modifier” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).
