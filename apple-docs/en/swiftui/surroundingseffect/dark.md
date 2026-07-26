---
title: dark
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 26.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/surroundingseffect/dark
source_url: 'https://developer.apple.com/documentation/swiftui/surroundingseffect/dark'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/surroundingseffect/dark.json'
content_hash: 'sha256:5bdce5c99ed29c0d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SurroundingsEffect](../surroundingseffect.md)

# dark

<sub>Type Property</sub>

An effect that dims passthrough video.

<sub>macOS, visionOS</sub>

```swift
static var dark: SurroundingsEffect { get }
```

## Discussion

Use this value with the [preferredSurroundingsEffect(_:)](<../view/preferredsurroundingseffect(__).md>) view modifier when you want to dim passthrough video while displaying a particular view. Doing so helps to draw attention to your app’s content while still enabling people to remain aware of their surroundings. This value can be used in the shared space.
