---
title: main
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+（26.0 起废弃）, iPadOS 2.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiscreen/main
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/main'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/main.json'
content_hash: 'sha256:671169ce993a063d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# main

<sub>Type Property</sub>

Returns the screen object representing the device’s screen.

> [!warning] Deprecated
> Use [screen](../uiwindowscene/screen.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class var main: UIScreen { get }
```

## Return Value

The screen object for the device.

## Discussion

Apple discourages the use of this symbol. Use a [UIScreen](../uiscreen.md) instance found through context instead. For example, reference the screen that displays a view through the [screen](../uiwindowscene/screen.md) property on the window scene managing the window containing the view.

## See Also

### Deprecated properties

- [screens](screens.md) — Returns an array containing all of the screens attached to the device. _(deprecated)_
- [applicationFrame](applicationframe.md) — The frame rectangle for the app window, measured in points. _(deprecated)_
- [focusedItem](focuseditem.md) — The item that is currently focused. _(deprecated)_
- [focusedView](focusedview.md) — The view that is currently focused. _(deprecated)_
- [supportsFocus](supportsfocus.md) — A Boolean value that indicates whether the screen supports focus-based inputs. _(deprecated)_
