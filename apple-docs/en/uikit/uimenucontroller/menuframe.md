---
title: menuFrame
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（16.0 起废弃）, iPadOS 3.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uimenucontroller/menuframe
source_url: 'https://developer.apple.com/documentation/uikit/uimenucontroller/menuframe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenucontroller/menuframe.json'
content_hash: 'sha256:072ce8899e1eb874'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuController](../uimenucontroller.md)

# menuFrame

<sub>Instance Property</sub>

Returns the frame of the editing menu.

> [!warning] Deprecated
> For more information, see [UIMenuController](../uimenucontroller.md).

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var menuFrame: CGRect { get }
```

## Discussion

The property value is the bounding rectangle of the menu in screen coordinates. The property has a value of [CGRectZero](../../coregraphics/cgrectzero.md) if the menu is not visible. You can use this property to adjust any user-interface objects away from the menu after displaying the menu.

## See Also

### Positioning the menu

- [arrowDirection](arrowdirection-swift.property.md) — The direction the arrow of the editing menu is pointing. _(deprecated)_
- [ArrowDirection](arrowdirection-swift.enum.md) — The direction the arrow of the editing menu is pointing. _(deprecated)_
- [- setTargetRect:inView:](<settargetrect(__in_).md>) — Sets the area in a view above or below which the editing menu is positioned. _(deprecated)_
