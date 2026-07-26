---
title: WindowInteractionBehavior
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/windowinteractionbehavior
source_url: 'https://developer.apple.com/documentation/swiftui/windowinteractionbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowinteractionbehavior.json'
content_hash: 'sha256:0e443597adcb0705'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# WindowInteractionBehavior

<sub>Structure</sub>

Options for enabling and disabling window interaction behaviors.

<sub>macOS</sub>

```swift
struct WindowInteractionBehavior
```

## Overview

Use values of this type in conjunction with the following view and scene modifiers to adjust the supported functionality for the window:

- [windowDismissBehavior(_:)](<view/windowdismissbehavior(__).md>)
- [windowMinimizeBehavior(_:)](<view/windowminimizebehavior(__).md>)
- [windowFullScreenBehavior(_:)](<view/windowfullscreenbehavior(__).md>)
- [windowResizeBehavior(_:)](<view/windowresizebehavior(__).md>)
- [windowBackgroundDragBehavior(_:)](<scene/windowbackgrounddragbehavior(__).md>)

For example, you can create a custom “About” window which only allows for dismissal:

```swift
struct MyApp: App {
    var body: some Scene {
        ...
        Window("About MyApp", id: "about") {
            AboutView()
                .windowMinimizeBehavior(.disabled)
                .windowResizeBehavior(.disabled)
        }
        .windowResizability(.contentSize)
    }
}
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [automatic](windowinteractionbehavior/automatic.md) — The automatic behavior. The associated window behavior will be enabled or disabled depending on the configuration of the enclosing `Scene`.
- [disabled](windowinteractionbehavior/disabled.md) — The disabled behavior. The associated window interaction behavior will be disabled.
- [enabled](windowinteractionbehavior/enabled.md) — The enabled behavior. The associated window interaction behavior will be enabled.

## See Also

### Managing window behavior

- [WindowManagerRole](windowmanagerrole.md) — Options for defining how a scene’s windows behave when used within a managed window context, such as full screen mode and Stage Manager.
- [windowManagerRole(_:)](<scene/windowmanagerrole(__).md>) — Configures the role for windows derived from `self` when participating in a managed window context, such as full screen or Stage Manager.
- [windowDismissBehavior(_:)](<view/windowdismissbehavior(__).md>) — Configures the dismiss functionality for the window enclosing `self`.
- [windowFullScreenBehavior(_:)](<view/windowfullscreenbehavior(__).md>) — Configures the full screen functionality for the window enclosing `self`.
- [windowMinimizeBehavior(_:)](<view/windowminimizebehavior(__).md>) — Configures the minimize functionality for the window enclosing `self`.
- [windowResizeBehavior(_:)](<view/windowresizebehavior(__).md>) — Configures the resize functionality for the window enclosing `self`.
- [windowBackgroundDragBehavior(_:)](<scene/windowbackgrounddragbehavior(__).md>) — Configures the behavior of dragging a window by its background.
- [allowsWindowActivationEvents()](<view/allowswindowactivationevents().md>) — Configures gestures in this view hierarchy to handle events that activate the containing window.
- [allowsWindowActivationEvents(_:)](<view/allowswindowactivationevents(__).md>) — Configures whether gestures in this view hierarchy can handle events that activate the containing window.
