---
title: 'windowBackgroundDragBehavior(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 15.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/windowbackgrounddragbehavior(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/windowbackgrounddragbehavior(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/windowbackgrounddragbehavior%28_%3A%29.json'
content_hash: 'sha256:f72dea0c0197a811'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# windowBackgroundDragBehavior(_:)

<sub>Instance Method</sub>

Configures the behavior of dragging a window by its background.

<sub>macOS</sub>

```swift
nonisolated func windowBackgroundDragBehavior(_ behavior: WindowInteractionBehavior) -> some Scene

```

## Parameters

- `behavior` — The behavior of dragging the modified window by its background.

## Return Value

A scene configured with the specified behavior of dragging it by its background background.

## Discussion

By default, or when you apply the [automatic](../windowinteractionbehavior/automatic.md) behavior, the system will determine the best suitable behavior based on the configuration of the modified scene.

You can use this modifier to override the default behavior. For example, to always enable dragging a window by its background:

```swift
struct MyApp: App {
    var body: some Scene {
        Window("About MyApp", id: "about") {
            AboutView()
        }
        .windowBackgroundDragBehavior(.enabled)
    }
}
```

If you want to let your users drag your window by a specific view instead of (or in addition to) letting them drag it by its background, use [WindowDragGesture](../windowdraggesture.md).

Applying the [enabled](../windowinteractionbehavior/enabled.md) behavior is equivalent to adding a [WindowDragGesture](../windowdraggesture.md) to the window’s background view.

## See Also

### Managing window behavior

- [WindowManagerRole](../windowmanagerrole.md) — Options for defining how a scene’s windows behave when used within a managed window context, such as full screen mode and Stage Manager.
- [windowManagerRole(_:)](<windowmanagerrole(__).md>) — Configures the role for windows derived from `self` when participating in a managed window context, such as full screen or Stage Manager.
- [WindowInteractionBehavior](../windowinteractionbehavior.md) — Options for enabling and disabling window interaction behaviors.
- [windowDismissBehavior(_:)](<../view/windowdismissbehavior(__).md>) — Configures the dismiss functionality for the window enclosing `self`.
- [windowFullScreenBehavior(_:)](<../view/windowfullscreenbehavior(__).md>) — Configures the full screen functionality for the window enclosing `self`.
- [windowMinimizeBehavior(_:)](<../view/windowminimizebehavior(__).md>) — Configures the minimize functionality for the window enclosing `self`.
- [windowResizeBehavior(_:)](<../view/windowresizebehavior(__).md>) — Configures the resize functionality for the window enclosing `self`.
- [allowsWindowActivationEvents()](<../view/allowswindowactivationevents().md>) — Configures gestures in this view hierarchy to handle events that activate the containing window.
- [allowsWindowActivationEvents(_:)](<../view/allowswindowactivationevents(__).md>) — Configures whether gestures in this view hierarchy can handle events that activate the containing window.
