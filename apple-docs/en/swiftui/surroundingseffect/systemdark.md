---
title: systemDark
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/surroundingseffect/systemdark
source_url: 'https://developer.apple.com/documentation/swiftui/surroundingseffect/systemdark'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/surroundingseffect/systemdark.json'
content_hash: 'sha256:c31da23181f01a8c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SurroundingsEffect](../surroundingseffect.md)

# systemDark

<sub>Type Property</sub>

An effect that dims passthrough video.

<sub>visionOS</sub>

```swift
static var systemDark: SurroundingsEffect { get }
```

## Discussion

Use this value with the [preferredSurroundingsEffect(_:)](<../view/preferredsurroundingseffect(__).md>) view modifier when you want to dim passthrough video while displaying a particular view. Doing so helps to draw attention to your app’s content while still enabling people to remain aware of their surroundings.
