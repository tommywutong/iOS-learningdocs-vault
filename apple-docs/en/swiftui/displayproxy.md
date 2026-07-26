---
title: DisplayProxy
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/displayproxy
source_url: 'https://developer.apple.com/documentation/swiftui/displayproxy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/displayproxy.json'
content_hash: 'sha256:4bbb3d5a1b381e60'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DisplayProxy

<sub>Structure</sub>

A type which provides information about display hardware.

<sub>macOS</sub>

```swift
struct DisplayProxy
```

## Overview

You can use this type with your custom window layouts to size and position windows relative to a display’s bounds.

For example, your custom window layout can position a window 140 points from the bottom of the screen’s visible area:

```swift
Window("Status", id: "status") {
    StatusView()
}
.windowResizability(.contentSize)
.defaultWindowPlacement { content, context in
    let displayBounds = context.defaultDisplay.visibleRect
    let size = content.sizeThatFits(.unspecified)
    let position = CGPoint(
        x: displayBounds.midX - (size.width / 2),
        y: displayBounds.maxY - size.height - 140)
    return WindowPlacement(position: position, size: size)
}
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md)

## Topics

### Instance Properties

- [bounds](displayproxy/bounds.md) — The full dimensions of the display, including any space occupied by system interface elements.
- [safeAreaInsets](displayproxy/safeareainsets.md) — The safe area inset of this display.
- [visibleRect](displayproxy/visiblerect.md) — The portion of the display where it is safe to place windows.

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
- [WindowProxy](windowproxy.md) — The proxy for an open window in the app.
