---
title: focusedItem
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+（15.0 起废弃）, iPadOS 10.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, tvOS 10.0+（15.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiscreen/focuseditem
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/focuseditem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/focuseditem.json'
content_hash: 'sha256:54d0201a3050cab6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# focusedItem

<sub>Instance Property</sub>

The item that is currently focused.

> [!warning] Deprecated
> Use [focusedItem](../uifocussystem/focuseditem.md) in [focusSystem](../uiwindowscene/focussystem.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
weak var focusedItem: (any UIFocusItem)? { get }
```

## Discussion

If this item is not a view, the [focusedView](focusedview.md) property is set to the view that contains the item.

## See Also

### Deprecated properties

- [mainScreen](main.md) — Returns the screen object representing the device’s screen. _(deprecated)_
- [screens](screens.md) — Returns an array containing all of the screens attached to the device. _(deprecated)_
- [applicationFrame](applicationframe.md) — The frame rectangle for the app window, measured in points. _(deprecated)_
- [focusedView](focusedview.md) — The view that is currently focused. _(deprecated)_
- [supportsFocus](supportsfocus.md) — A Boolean value that indicates whether the screen supports focus-based inputs. _(deprecated)_
