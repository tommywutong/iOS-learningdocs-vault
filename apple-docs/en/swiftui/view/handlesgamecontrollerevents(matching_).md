---
title: 'handlesGameControllerEvents(matching:)'
framework: GameController
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/handlesgamecontrollerevents(matching:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/handlesgamecontrollerevents(matching:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/handlesgamecontrollerevents%28matching%3A%29.json'
content_hash: 'sha256:237297cfa23c752e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# handlesGameControllerEvents(matching:)

<sub>Instance Method</sub>

Specifies the game controllers events which should be delivered through the GameController framework when the view, or one of its descendants has focus.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated func handlesGameControllerEvents(matching types: GCUIEventTypes) -> some View

```

## Discussion

```swift
SpriteView(scene: MyGameScene())
.handlesGameControllerEvents(matching: .gamepad)
.focused(true)
```
