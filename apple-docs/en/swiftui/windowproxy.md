---
title: WindowProxy
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/windowproxy
source_url: 'https://developer.apple.com/documentation/swiftui/windowproxy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowproxy.json'
content_hash: 'sha256:f7b5e4a0d1c5189b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# WindowProxy

<sub>Structure</sub>

The proxy for an open window in the app.

<sub>visionOS</sub>

```swift
struct WindowProxy
```

## Topics

### Instance Properties

- [id](windowproxy/id.md) — The ID for the window, if one was provided.
- [phase](windowproxy/phase.md) — The window’s current [ScenePhase](scenephase.md).

## See Also

### Positioning a window

- [defaultPosition(_:)](<scene/defaultposition(__).md>) — Sets a default position for a window.
- [WindowLevel](windowlevel.md) — The level of a window.
- [windowLevel(_:)](<scene/windowlevel(__).md>) — Sets the window level of this scene.
- [WindowLayoutRoot](windowlayoutroot.md) — A proxy which represents the root contents of a window.
- [WindowPlacement](windowplacement.md) — A type which represents a preferred size and position for a window.
- [defaultWindowPlacement(_:)](<scene/defaultwindowplacement(__).md>) — Defines a function used for determining the default placement of windows.
- [windowIdealPlacement(_:)](<scene/windowidealplacement(__).md>) — Provides a function which determines a placement to use when windows of a scene zoom.
- [WindowPlacementContext](windowplacementcontext.md) — A type which represents contextual information used for sizing and positioning windows.
- [DisplayProxy](displayproxy.md) — A type which provides information about display hardware.
