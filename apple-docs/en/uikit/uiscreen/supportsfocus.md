---
title: supportsFocus
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（15.0 起废弃）, iPadOS 9.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, tvOS 9.0+（15.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiscreen/supportsfocus
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/supportsfocus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/supportsfocus.json'
content_hash: 'sha256:2c738994c56b9072'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# supportsFocus

<sub>Instance Property</sub>

A Boolean value that indicates whether the screen supports focus-based inputs.

> [!warning] Deprecated
> Use [focusSystem](../uiwindowscene/focussystem.md) `!= nil` instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var supportsFocus: Bool { get }
```

## See Also

### Deprecated properties

- [mainScreen](main.md) — Returns the screen object representing the device’s screen. _(deprecated)_
- [screens](screens.md) — Returns an array containing all of the screens attached to the device. _(deprecated)_
- [applicationFrame](applicationframe.md) — The frame rectangle for the app window, measured in points. _(deprecated)_
- [focusedItem](focuseditem.md) — The item that is currently focused. _(deprecated)_
- [focusedView](focusedview.md) — The view that is currently focused. _(deprecated)_
