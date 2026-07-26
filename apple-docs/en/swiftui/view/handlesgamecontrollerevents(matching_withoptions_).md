---
title: 'handlesGameControllerEvents(matching:withOptions:)'
framework: GameController
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/handlesgamecontrollerevents(matching:withoptions:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/handlesgamecontrollerevents(matching:withoptions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/handlesgamecontrollerevents%28matching%3Awithoptions%3A%29.json'
content_hash: 'sha256:759a90cd7a152e2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# handlesGameControllerEvents(matching:withOptions:)

<sub>Instance Method</sub>

Specifies the game controllers events which should be delivered through the GameController framework when the view or one of its descendants has focus.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated func handlesGameControllerEvents(matching types: GCUIEventTypes, withOptions options: GameControllerEventHandlingOptions?) -> some View

```

## Discussion

```swift
SpriteView(scene: MyGameScene())
.handlesGameControllerEvents(matching: .gamepad, withOptions: .defaultOptions)
.focused(true)
```

## See Also

### Game controller

- [handlesGameControllerEvents(matching:)](<handlesgamecontrollerevents(matching_).md>) — Specifies the game controllers events which should be delivered through the GameController framework when the view, or one of its descendants has focus.
