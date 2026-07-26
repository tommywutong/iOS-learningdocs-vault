---
title: UIWindow.Level
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindow/level
source_url: 'https://developer.apple.com/documentation/uikit/uiwindow/level'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindow/level.json'
content_hash: 'sha256:d05fcf61564cadb4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindow](../uiwindow.md)

# UIWindow.Level

<sub>Structure</sub>

The positioning of windows relative to each other.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct Level
```

## Overview

The stacking of levels takes precedence over the stacking of windows within each level. That is, even the bottom window in a level obscures the top window of the next level down. Levels are listed in order from lowest to highest.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Comparable](../../swift/comparable.md), [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Window levels

- [UIWindowLevelNormal](level/normal.md) — The default level.
- [UIWindowLevelStatusBar](level/statusbar.md) — The level for a status window.
- [UIWindowLevelAlert](level/alert.md) — The level for an alert view.

### Initializers

- [init(_:)](<level/init(__).md>) — Creates a window level structure.
- [init(rawValue:)](<level/init(rawvalue_).md>) — Creates a window level structure with the specified raw value.

## See Also

### Configuring the window

- [rootViewController](rootviewcontroller.md) — The root view controller for the window.
- [windowLevel](windowlevel.md) — The position of the window in the z-axis.
- [canResizeToFitContent](canresizetofitcontent.md) — A Boolean value that indicates whether the window’s constraint-based content determines its size.
- [screen](screen.md) — The screen to display the window on. _(deprecated)_
