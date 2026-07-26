---
title: ultraDark
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 26.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/surroundingseffect/ultradark
source_url: 'https://developer.apple.com/documentation/swiftui/surroundingseffect/ultradark'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/surroundingseffect/ultradark.json'
content_hash: 'sha256:0677f19e57512fcb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SurroundingsEffect](../surroundingseffect.md)

# ultraDark

<sub>Type Property</sub>

An effect that dims passthrough video more than [dark](dark.md)

<sub>macOS, visionOS</sub>

```swift
static var ultraDark: SurroundingsEffect { get }
```

## Discussion

Use this value with the [preferredSurroundingsEffect(_:)](<../view/preferredsurroundingseffect(__).md>) view modifier when you want to dim passthrough video while displaying a particular view. Doing so helps to draw attention to your app’s content while still enabling people to remain aware of their surroundings. This effect will only be applied while an immersive space is opened.
