---
title: 'dim(intensity:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 26.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/surroundingseffect/dim(intensity:)'
source_url: 'https://developer.apple.com/documentation/swiftui/surroundingseffect/dim(intensity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/surroundingseffect/dim%28intensity%3A%29.json'
content_hash: 'sha256:a4e755531d68872f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SurroundingsEffect](../surroundingseffect.md)

# dim(intensity:)

<sub>Type Method</sub>

An effect that dims the passthrough video a custom amount.

<sub>macOS, visionOS</sub>

```swift
static func dim(intensity: Double) -> SurroundingsEffect
```

## Discussion

Use this with the [preferredSurroundingsEffect(_:)](<../view/preferredsurroundingseffect(__).md>) view modifier when you want to darken the passthrough while displaying a particular view. The value will be clamped between 0 and 1. This effect will only be applied while an immersive space is opened.
