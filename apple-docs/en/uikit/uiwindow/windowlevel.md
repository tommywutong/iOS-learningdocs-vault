---
title: windowLevel
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindow/windowlevel
source_url: 'https://developer.apple.com/documentation/uikit/uiwindow/windowlevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindow/windowlevel.json'
content_hash: 'sha256:31049638cd15b6aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindow](../uiwindow.md)

# windowLevel

<sub>Instance Property</sub>

The position of the window in the z-axis.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var windowLevel: UIWindow.Level { get set }
```

## Discussion

Window levels provide a relative grouping of windows along the z-axis. All windows assigned to the same window level appear in front of (or behind) all windows assigned to a different window level. The ordering of windows within a given window level is not guaranteed.

The default value of this property is [UIWindowLevelNormal](level/normal.md). For a list of other possible window levels, see [Level](level.md).

## See Also

### Configuring the window

- [rootViewController](rootviewcontroller.md) — The root view controller for the window.
- [Level](level.md) — The positioning of windows relative to each other.
- [canResizeToFitContent](canresizetofitcontent.md) — A Boolean value that indicates whether the window’s constraint-based content determines its size.
- [screen](screen.md) — The screen to display the window on. _(deprecated)_
