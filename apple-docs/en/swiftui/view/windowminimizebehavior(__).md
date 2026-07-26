---
title: 'windowMinimizeBehavior(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 15.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/windowminimizebehavior(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/windowminimizebehavior(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/windowminimizebehavior%28_%3A%29.json'
content_hash: 'sha256:b57b0c378a7a3e7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# windowMinimizeBehavior(_:)

<sub>Instance Method</sub>

Configures the minimize functionality for the window enclosing `self`.

<sub>macOS</sub>

```swift
nonisolated func windowMinimizeBehavior(_ behavior: WindowInteractionBehavior) -> some View

```

## Parameters

- `behavior` — The resize behavior.

## Discussion

On macOS, windows which support being minimized will move into the Dock when the minimize button is clicked, or the corresponding menu item is selected.

By default, the window minimize functionality is determined by the scene, as well as any modifiers applied to it.

You can use this modifier to override the default behavior.

For example, you can create a custom “About” window which disables the minimize functionality:

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
- [windowResizeBehavior(_:)](<windowresizebehavior(__).md>) — Configures the resize functionality for the window enclosing `self`.
- [windowBackgroundDragBehavior(_:)](<../scene/windowbackgrounddragbehavior(__).md>) — Configures the behavior of dragging a window by its background.
- [allowsWindowActivationEvents()](<allowswindowactivationevents().md>) — Configures gestures in this view hierarchy to handle events that activate the containing window.
- [allowsWindowActivationEvents(_:)](<allowswindowactivationevents(__).md>) — Configures whether gestures in this view hierarchy can handle events that activate the containing window.
