---
title: applicationFrame
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiscreen/applicationframe
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/applicationframe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/applicationframe.json'
content_hash: 'sha256:a3272d21fe0c89d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# applicationFrame

<sub>Instance Property</sub>

The frame rectangle for the app window, measured in points.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var applicationFrame: CGRect { get }
```

## Discussion

This property contains the bounds rectangle used by the app window, which may be different than the screen bounds themselves. This rectangle is specified in the current coordinate space, which takes into account any interface rotations in effect for the device. Therefore, the value of this property may change when the device rotates between portrait and landscape orientations.

## See Also

### Deprecated properties

- [mainScreen](main.md) — Returns the screen object representing the device’s screen. _(deprecated)_
- [screens](screens.md) — Returns an array containing all of the screens attached to the device. _(deprecated)_
- [focusedItem](focuseditem.md) — The item that is currently focused. _(deprecated)_
- [focusedView](focusedview.md) — The view that is currently focused. _(deprecated)_
- [supportsFocus](supportsfocus.md) — A Boolean value that indicates whether the screen supports focus-based inputs. _(deprecated)_
