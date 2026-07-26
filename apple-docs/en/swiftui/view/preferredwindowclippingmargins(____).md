---
title: 'preferredWindowClippingMargins(_:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/preferredwindowclippingmargins(_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/preferredwindowclippingmargins(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/preferredwindowclippingmargins%28_%3A_%3A%29.json'
content_hash: 'sha256:ca40fadcb0b2dfea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# preferredWindowClippingMargins(_:_:)

<sub>Instance Method</sub>

Requests additional margins for drawing beyond the bounds of the window.

<sub>visionOS</sub>

```swift
@MainActor @preconcurrency func preferredWindowClippingMargins(_ edges: Edge3D.Set = .all, _ length: CGFloat?) -> some View

```

## Parameters

- `edges` — The edges that should receive margins.

- `length` — The amount of margin requested on each specified edge.

## Discussion

This modifier will only have an effect on windows with a `.volumetric` window style.

A window’s bounds are based on its content, and resizable by dragging the corners. By default, the system clips any content that draws beyond the bounds. This modifier requests additional space for drawing outside the window’s bounds. Use this space to render extra visual effects that enhance the impact of your app. This content does not receive events, and may be clipped by the system at any time.

The additional margins granted by this modifier are not guaranteed, and the system may update or reduce them. Any time the system updates the current margins, it will update the `windowClippingMargins` value in the environment.

If multiple views request margins, the scene’s preferred margins will be the maximum preferred value for each face. For example, if one view wants a leading margin of `400` and another view a trailing margin of `400`, the scene will request both a leading and trailing margin of `400`. If one view requests a leading margin of `200` and another view a leading margin of `300`, the scene will request `300`.

## See Also

### Window behaviors

- [windowDismissBehavior(_:)](<windowdismissbehavior(__).md>) — Configures the dismiss functionality for the window enclosing `self`.
- [windowFullScreenBehavior(_:)](<windowfullscreenbehavior(__).md>) — Configures the full screen functionality for the window enclosing `self`.
- [windowToolbarFullScreenVisibility(_:)](<windowtoolbarfullscreenvisibility(__).md>) — Configures the visibility of the window toolbar when the window enters full screen mode.
- [windowMinimizeBehavior(_:)](<windowminimizebehavior(__).md>) — Configures the minimize functionality for the window enclosing `self`.
- [windowResizeAnchor(_:)](<windowresizeanchor(__).md>) — Sets the window anchor point used when the size of the view changes such that the window must resize.
- [windowResizeBehavior(_:)](<windowresizebehavior(__).md>) — Configures the resize functionality for the window enclosing `self`.
