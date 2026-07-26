---
title: 'windowManagerRole(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/windowmanagerrole(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/windowmanagerrole(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/windowmanagerrole%28_%3A%29.json'
content_hash: 'sha256:f53aa8893404d689'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# windowManagerRole(_:)

<sub>Instance Method</sub>

Configures the role for windows derived from `self` when participating in a managed window context, such as full screen or Stage Manager.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func windowManagerRole(_ role: WindowManagerRole) -> some Scene

```

## Discussion

By default, the type of `Scene` and its placement within the app’s definition will determine the behavior of its windows within a window management context.

You can use this modifier to override the default behaivor.

For example, you can specify that a secondary `Window` scene should use the principal behavior for full screen and Stage Manager:

```swift
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        Window("Organizer", id: "organizer") {
            OrganizerView()
        }
        .windowManagerRole(.principal)
    }
}
```

## See Also

### Managing window behavior

- [WindowManagerRole](../windowmanagerrole.md) — Options for defining how a scene’s windows behave when used within a managed window context, such as full screen mode and Stage Manager.
- [WindowInteractionBehavior](../windowinteractionbehavior.md) — Options for enabling and disabling window interaction behaviors.
- [windowDismissBehavior(_:)](<../view/windowdismissbehavior(__).md>) — Configures the dismiss functionality for the window enclosing `self`.
- [windowFullScreenBehavior(_:)](<../view/windowfullscreenbehavior(__).md>) — Configures the full screen functionality for the window enclosing `self`.
- [windowMinimizeBehavior(_:)](<../view/windowminimizebehavior(__).md>) — Configures the minimize functionality for the window enclosing `self`.
- [windowResizeBehavior(_:)](<../view/windowresizebehavior(__).md>) — Configures the resize functionality for the window enclosing `self`.
- [windowBackgroundDragBehavior(_:)](<windowbackgrounddragbehavior(__).md>) — Configures the behavior of dragging a window by its background.
- [allowsWindowActivationEvents()](<../view/allowswindowactivationevents().md>) — Configures gestures in this view hierarchy to handle events that activate the containing window.
- [allowsWindowActivationEvents(_:)](<../view/allowswindowactivationevents(__).md>) — Configures whether gestures in this view hierarchy can handle events that activate the containing window.
