---
title: 'colorMultiply(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 26.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/surroundingseffect/colormultiply(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/surroundingseffect/colormultiply(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/surroundingseffect/colormultiply%28_%3A%29.json'
content_hash: 'sha256:c83c5f3212e787e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SurroundingsEffect](../surroundingseffect.md)

# colorMultiply(_:)

<sub>Type Method</sub>

An effect that applies a custom tint to the passthrough video by multiplying the passthrough with a [Color](../color.md).

<sub>macOS, visionOS</sub>

```swift
static func colorMultiply(_ color: Color) -> SurroundingsEffect
```

## Parameters

- `color` — The color to bias the passthrough toward. The opacity of the color is ignored. Use the extended color space to brighten the passthrough.

## Discussion

Use this with the [preferredSurroundingsEffect(_:)](<../view/preferredsurroundingseffect(__).md>) view modifier when you want to tint the passthrough while displaying a particular view. The system may decide to limit how much each color in the passthrough can be brightened or darkened. `Color.black` will cause no passthrough to be visible, and `Color.white` will have no effect. `Color(red: 1.15, green: 1.0, blue: 1.0)` would brighten the red in the passthrough by 15 percent. This effect will only be applied while an immersive space is opened.
