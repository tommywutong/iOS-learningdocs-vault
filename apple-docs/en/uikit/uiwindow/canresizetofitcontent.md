---
title: canResizeToFitContent
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindow/canresizetofitcontent
source_url: 'https://developer.apple.com/documentation/uikit/uiwindow/canresizetofitcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindow/canresizetofitcontent.json'
content_hash: 'sha256:8d4cd8c3f875472c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindow](../uiwindow.md)

# canResizeToFitContent

<sub>Instance Property</sub>

A Boolean value that indicates whether the window’s constraint-based content determines its size.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var canResizeToFitContent: Bool { get set }
```

## Discussion

The default value of this property is [false](../../swift/false.md), which causes the window to maintain a fixed size. Setting this property to [true](../../swift/true.md) allows the system to perform constraints-based window sizing, which updates the window’s size to match the space needed by its content. Window-size changes occur only when the app runs on macOS.

## See Also

### Configuring the window

- [rootViewController](rootviewcontroller.md) — The root view controller for the window.
- [windowLevel](windowlevel.md) — The position of the window in the z-axis.
- [Level](level.md) — The positioning of windows relative to each other.
- [screen](screen.md) — The screen to display the window on. _(deprecated)_
