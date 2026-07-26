---
title: semiDark
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 26.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/surroundingseffect/semidark
source_url: 'https://developer.apple.com/documentation/swiftui/surroundingseffect/semidark'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/surroundingseffect/semidark.json'
content_hash: 'sha256:4146dde7445e1de7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SurroundingsEffect](../surroundingseffect.md)

# semiDark

<sub>Type Property</sub>

An effect that dims passthrough video less than [dark](dark.md).

<sub>macOS, visionOS</sub>

```swift
static var semiDark: SurroundingsEffect { get }
```

## Discussion

Use this value with the [preferredSurroundingsEffect(_:)](<../view/preferredsurroundingseffect(__).md>) view modifier when you want to dim passthrough video while displaying a particular view. Doing so helps to draw attention to your app’s content while still enabling people to remain aware of their surroundings. This value can be used in the shared space.
