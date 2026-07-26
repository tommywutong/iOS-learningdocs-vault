---
title: 'windowResizeBehavior(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 15.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/windowresizebehavior(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/windowresizebehavior(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/windowresizebehavior%28_%3A%29.json'
content_hash: 'sha256:68e51dd365abe3e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# windowResizeBehavior(_:)

<sub>Instance Method</sub>

Configures the resize functionality for the window enclosing `self`.

<sub>macOS</sub>

```swift
nonisolated func windowResizeBehavior(_ behavior: WindowInteractionBehavior) -> some View

```

## Parameters

- `behavior` — The resize behavior.

## Discussion

By default, the window resizability functionality is determined by the scene, as well as any modifiers applied to it. Additionally, when using the [windowResizability(_:)](<../scene/windowresizability(__).md>) modifier, the minimum and maximum size of the window’s contents will also determine the resizability behavior.

You can use this modifier to override the default behavior.

For example, you can create a custom “About” window which only allows for dismissal:

```swift
struct MyApp: App {
    var body: some Scene {
        ...
        Window("About MyApp", id: "about") {
            AboutView()
                .windowResizeBehavior(.disabled)
                .windowMinimizeBehavior(.disabled)
        }
        .windowResizability(.contentSize)
    }
}
```

## See Also

### Managing window behavior

- [WindowManagerRole](../windowmanagerrole.md) — Options for defining how a scene’s windows behave when used within a managed window context, such as full screen mode and Stage Manager.
- [windowManagerRole(_:)](<../scene/windowmanagerrole(__).md>) — Configures the role for windows derived from `self` when participating in a managed window context, such as full screen or Stage Manager.
- [WindowInteractionBehavior](../windowinteractionbehavior.md) — Options for enabling and disabling window interaction behaviors.
- [windowDismissBehavior(_:)](<windowdismissbehavior(__).md>) — Configures the dismiss functionality for the window enclosing `self`.
- [windowFullScreenBehavior(_:)](<windowfullscreenbehavior(__).md>) — Configures the full screen functionality for the window enclosing `self`.
- [windowMinimizeBehavior(_:)](<windowminimizebehavior(__).md>) — Configures the minimize functionality for the window enclosing `self`.
- [windowBackgroundDragBehavior(_:)](<../scene/windowbackgrounddragbehavior(__).md>) — Configures the behavior of dragging a window by its background.
- [allowsWindowActivationEvents()](<allowswindowactivationevents().md>) — Configures gestures in this view hierarchy to handle events that activate the containing window.
- [allowsWindowActivationEvents(_:)](<allowswindowactivationevents(__).md>) — Configures whether gestures in this view hierarchy can handle events that activate the containing window.
