---
title: WindowLayoutRoot
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 15.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/windowlayoutroot
source_url: 'https://developer.apple.com/documentation/swiftui/windowlayoutroot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowlayoutroot.json'
content_hash: 'sha256:3158d886ea0337e8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# WindowLayoutRoot

<sub>Structure</sub>

A proxy which represents the root contents of a window.

<sub>macOS, visionOS</sub>

```swift
struct WindowLayoutRoot
```

## Overview

This type acts like a proxy for the contents of the window defined by a SwiftUI [Scene](scene.md). The `Scene.defaultWindowPlacement(_:)` modifier receives an instance of this type, representing the contents of the window being created.

Use this proxy to get information about the window’s contents, like it’s size.

## Topics

### Instance Methods

- [sizeThatFits(_:)](<windowlayoutroot/sizethatfits(__).md>) — Asks the window’s content for its size.

## See Also

### Positioning a window

- [defaultPosition(_:)](<scene/defaultposition(__).md>) — Sets a default position for a window.
- [WindowLevel](windowlevel.md) — The level of a window.
- [windowLevel(_:)](<scene/windowlevel(__).md>) — Sets the window level of this scene.
- [WindowPlacement](windowplacement.md) — A type which represents a preferred size and position for a window.
- [defaultWindowPlacement(_:)](<scene/defaultwindowplacement(__).md>) — Defines a function used for determining the default placement of windows.
- [windowIdealPlacement(_:)](<scene/windowidealplacement(__).md>) — Provides a function which determines a placement to use when windows of a scene zoom.
- [WindowPlacementContext](windowplacementcontext.md) — A type which represents contextual information used for sizing and positioning windows.
- [WindowProxy](windowproxy.md) — The proxy for an open window in the app.
- [DisplayProxy](displayproxy.md) — A type which provides information about display hardware.
