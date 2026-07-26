---
title: allowsWindowActivationEvents()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view/allowswindowactivationevents()
source_url: 'https://developer.apple.com/documentation/swiftui/view/allowswindowactivationevents()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/allowswindowactivationevents%28%29.json'
content_hash: 'sha256:ec07c35cd9ebf0c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# allowsWindowActivationEvents()

<sub>Instance Method</sub>

Configures gestures in this view hierarchy to handle events that activate the containing window.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated func allowsWindowActivationEvents() -> some View

```

## Discussion

Views higher in the hierarchy can override the value you set on this view. In the following example, the tap gesture on the `Rectangle` won’t handle events that activate the containing window because the outer `allowsWindowActivationEvents(_:)` view modifier overrides the inner one:

```swift
HStack {
    Rectangle()
        .onTapGesture { ... }
        .allowsWindowActivationEvents()
}
.allowsWindowActivationEvents(false)
```

> [!note] Note
> It’s only possible to disallow handling events that activate the containing window for views that allow it by default or that inherit this behavior from their ancestors. Views that explicitly already disallow this functionality can’t have it turned on.

## See Also

### Managing window behavior

- [WindowManagerRole](../windowmanagerrole.md) — Options for defining how a scene’s windows behave when used within a managed window context, such as full screen mode and Stage Manager.
- [windowManagerRole(_:)](<../scene/windowmanagerrole(__).md>) — Configures the role for windows derived from `self` when participating in a managed window context, such as full screen or Stage Manager.
- [WindowInteractionBehavior](../windowinteractionbehavior.md) — Options for enabling and disabling window interaction behaviors.
- [windowDismissBehavior(_:)](<windowdismissbehavior(__).md>) — Configures the dismiss functionality for the window enclosing `self`.
- [windowFullScreenBehavior(_:)](<windowfullscreenbehavior(__).md>) — Configures the full screen functionality for the window enclosing `self`.
- [windowMinimizeBehavior(_:)](<windowminimizebehavior(__).md>) — Configures the minimize functionality for the window enclosing `self`.
- [windowResizeBehavior(_:)](<windowresizebehavior(__).md>) — Configures the resize functionality for the window enclosing `self`.
- [windowBackgroundDragBehavior(_:)](<../scene/windowbackgrounddragbehavior(__).md>) — Configures the behavior of dragging a window by its background.
- [allowsWindowActivationEvents(_:)](<allowswindowactivationevents(__).md>) — Configures whether gestures in this view hierarchy can handle events that activate the containing window.
