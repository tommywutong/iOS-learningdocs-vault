---
title: screen
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiwindow/screen
source_url: 'https://developer.apple.com/documentation/uikit/uiwindow/screen'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindow/screen.json'
content_hash: 'sha256:fd0c0f5bb1159770'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindow](../uiwindow.md)

# screen

<sub>Instance Property</sub>

The screen to display the window on.

> [!warning] Deprecated
> Use [windowScene](windowscene.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var screen: UIScreen { get set }
```

## Discussion

By default, UIKit sets this property to the primary device screen. If additional screens are attached to the device, you can assign a different screen object to display the window on that screen. A window is always displayed on only one screen.

Moving windows from screen to screen is a relatively expensive operation and isn’t optimal in performance-sensitive code. Instead, change the screen before displaying the window the first time. Changing the screen of a window that hasn’t been ordered onto the screen has no significant additional cost.

## See Also

### Configuring the window

- [rootViewController](rootviewcontroller.md) — The root view controller for the window.
- [windowLevel](windowlevel.md) — The position of the window in the z-axis.
- [Level](level.md) — The positioning of windows relative to each other.
- [canResizeToFitContent](canresizetofitcontent.md) — A Boolean value that indicates whether the window’s constraint-based content determines its size.
