---
title: WindowPlacementContext
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 15.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/windowplacementcontext
source_url: 'https://developer.apple.com/documentation/swiftui/windowplacementcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowplacementcontext.json'
content_hash: 'sha256:922fff3621a5cfea'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# WindowPlacementContext

<sub>Structure</sub>

A type which represents contextual information used for sizing and positioning windows.

<sub>macOS, visionOS</sub>

```swift
struct WindowPlacementContext
```

## Overview

The placement context provides information to be used when providing a new placement via the closure provided to the `defaultWindowPlacement(_:)` modifier.

## Topics

### Instance Properties

- [defaultDisplay](windowplacementcontext/defaultdisplay.md) — The display on which new windows will be presented by default.
- [windows](windowplacementcontext/windows.md) — The list of current active scenes

## See Also

### Positioning a window

- [defaultPosition(_:)](<scene/defaultposition(__).md>) — Sets a default position for a window.
- [WindowLevel](windowlevel.md) — The level of a window.
- [windowLevel(_:)](<scene/windowlevel(__).md>) — Sets the window level of this scene.
- [WindowLayoutRoot](windowlayoutroot.md) — A proxy which represents the root contents of a window.
- [WindowPlacement](windowplacement.md) — A type which represents a preferred size and position for a window.
- [defaultWindowPlacement(_:)](<scene/defaultwindowplacement(__).md>) — Defines a function used for determining the default placement of windows.
- [windowIdealPlacement(_:)](<scene/windowidealplacement(__).md>) — Provides a function which determines a placement to use when windows of a scene zoom.
- [WindowProxy](windowproxy.md) — The proxy for an open window in the app.
- [DisplayProxy](displayproxy.md) — A type which provides information about display hardware.
