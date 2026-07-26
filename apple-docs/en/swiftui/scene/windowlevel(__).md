---
title: 'windowLevel(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 15.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/windowlevel(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/windowlevel(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/windowlevel%28_%3A%29.json'
content_hash: 'sha256:40f1cd4ada7aa448'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# windowLevel(_:)

<sub>Instance Method</sub>

Sets the window level of this scene.

<sub>macOS</sub>

```swift
nonisolated func windowLevel(_ level: WindowLevel) -> some Scene

```

## Parameters

- `level` — The desired window level

## Discussion

```swift
Window("Utility Window", id: "...") {
    UtilityContent()
}
.windowLevel(.floating)
```

## See Also

### Positioning a window

- [defaultPosition(_:)](<defaultposition(__).md>) — Sets a default position for a window.
- [WindowLevel](../windowlevel.md) — The level of a window.
- [WindowLayoutRoot](../windowlayoutroot.md) — A proxy which represents the root contents of a window.
- [WindowPlacement](../windowplacement.md) — A type which represents a preferred size and position for a window.
- [defaultWindowPlacement(_:)](<defaultwindowplacement(__).md>) — Defines a function used for determining the default placement of windows.
- [windowIdealPlacement(_:)](<windowidealplacement(__).md>) — Provides a function which determines a placement to use when windows of a scene zoom.
- [WindowPlacementContext](../windowplacementcontext.md) — A type which represents contextual information used for sizing and positioning windows.
- [WindowProxy](../windowproxy.md) — The proxy for an open window in the app.
- [DisplayProxy](../displayproxy.md) — A type which provides information about display hardware.
