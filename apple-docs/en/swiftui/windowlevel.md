---
title: WindowLevel
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/windowlevel
source_url: 'https://developer.apple.com/documentation/swiftui/windowlevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowlevel.json'
content_hash: 'sha256:9f8f9ee91fc1615d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# WindowLevel

<sub>Structure</sub>

The level of a window.

<sub>macOS</sub>

```swift
struct WindowLevel
```

## Overview

Use this in conjunction with the `.windowLevel(_:)` modifier to control window levels.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [automatic](windowlevel/automatic.md) — Automatic window level.
- [desktop](windowlevel/desktop.md) — Desktop window level.
- [floating](windowlevel/floating.md) — Floating window level.
- [normal](windowlevel/normal.md) — Normal window level.

## See Also

### Positioning a window

- [defaultPosition(_:)](<scene/defaultposition(__).md>) — Sets a default position for a window.
- [windowLevel(_:)](<scene/windowlevel(__).md>) — Sets the window level of this scene.
- [WindowLayoutRoot](windowlayoutroot.md) — A proxy which represents the root contents of a window.
- [WindowPlacement](windowplacement.md) — A type which represents a preferred size and position for a window.
- [defaultWindowPlacement(_:)](<scene/defaultwindowplacement(__).md>) — Defines a function used for determining the default placement of windows.
- [windowIdealPlacement(_:)](<scene/windowidealplacement(__).md>) — Provides a function which determines a placement to use when windows of a scene zoom.
- [WindowPlacementContext](windowplacementcontext.md) — A type which represents contextual information used for sizing and positioning windows.
- [WindowProxy](windowproxy.md) — The proxy for an open window in the app.
- [DisplayProxy](displayproxy.md) — A type which provides information about display hardware.
