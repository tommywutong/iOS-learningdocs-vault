---
title: screens
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.2+（16.0 起废弃）, iPadOS 3.2+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, tvOS（16.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiscreen/screens
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/screens'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/screens.json'
content_hash: 'sha256:99dc0c57152837c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# screens

<sub>Type Property</sub>

Returns an array containing all of the screens attached to the device.

> [!warning] Deprecated
> Use [openSessions](../uiapplication/opensessions.md) on the shared app object to find scenes for other screens.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class var screens: [UIScreen] { get }
```

## Return Value

An array of `UIScreen` objects.

## Discussion

The returned array includes the main screen plus any additional screens connected to the device. The main screen is always at index `0`.

Not all devices support external displays. iPhone and iPod touch devices with Retina displays and iPads support external displays. Older devices, such as the iPhone 3GS, don’t support external displays.

## See Also

### Deprecated properties

- [mainScreen](main.md) — Returns the screen object representing the device’s screen. _(deprecated)_
- [applicationFrame](applicationframe.md) — The frame rectangle for the app window, measured in points. _(deprecated)_
- [focusedItem](focuseditem.md) — The item that is currently focused. _(deprecated)_
- [focusedView](focusedview.md) — The view that is currently focused. _(deprecated)_
- [supportsFocus](supportsfocus.md) — A Boolean value that indicates whether the screen supports focus-based inputs. _(deprecated)_
