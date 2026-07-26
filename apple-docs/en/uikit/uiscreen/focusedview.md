---
title: focusedView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（15.0 起废弃）, iPadOS 9.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, tvOS 9.0+（15.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiscreen/focusedview
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/focusedview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/focusedview.json'
content_hash: 'sha256:163d5f9f59e3f344'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# focusedView

<sub>Instance Property</sub>

The view that is currently focused.

> [!warning] Deprecated
> Use [focusedItem](../uifocussystem/focuseditem.md) in [focusSystem](../uiwindowscene/focussystem.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
weak var focusedView: UIView? { get }
```

## Discussion

When a view has focus, this property contains that view. When the focus is on an item that is not a view, the view in this property is the one that contains the item. This property is `nil` when nothing is currently focused on the screen.

## See Also

### Deprecated properties

- [mainScreen](main.md) — Returns the screen object representing the device’s screen. _(deprecated)_
- [screens](screens.md) — Returns an array containing all of the screens attached to the device. _(deprecated)_
- [applicationFrame](applicationframe.md) — The frame rectangle for the app window, measured in points. _(deprecated)_
- [focusedItem](focuseditem.md) — The item that is currently focused. _(deprecated)_
- [supportsFocus](supportsfocus.md) — A Boolean value that indicates whether the screen supports focus-based inputs. _(deprecated)_
