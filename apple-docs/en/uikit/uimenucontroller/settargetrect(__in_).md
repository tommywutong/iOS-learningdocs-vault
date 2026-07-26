---
title: 'setTargetRect(_:in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（13.0 起废弃）, iPadOS 3.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uimenucontroller/settargetrect(_:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uimenucontroller/settargetrect(_:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenucontroller/settargetrect%28_%3Ain%3A%29.json'
content_hash: 'sha256:0a805fb36719347d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuController](../uimenucontroller.md)

# setTargetRect(_:in:)

<sub>Instance Method</sub>

Sets the area in a view above or below which the editing menu is positioned.

> [!warning] Deprecated
> For more information, see [UIMenuController](../uimenucontroller.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func setTargetRect(_ targetRect: CGRect, in targetView: UIView)
```

## Parameters

- `targetRect` — A rectangle that defines the area that is to be the target of the menu commands.

- `targetView` — The view in which `targetRect` appears.

## Discussion

This target rectangle (`targetRect`) is usually the bounding rectangle of a selection. `UIMenuController` positions the editing menu above this rectangle; if there is not enough space for the menu there, it positions it below the rectangle. The menu’s pointer is placed at the center of the top or bottom of the target rectangle as appropriate. Note that if you make the width or height of the target rectangle zero, `UIMenuController` treats the target area as a line or point for positioning (for example, an insertion caret or a single point).

Once it is set, the target rectangle does not track the view; if the view moves (such as would happen in a scroll view), you must update the target rectangle accordingly.

## See Also

### Positioning the menu

- [menuFrame](menuframe.md) — Returns the frame of the editing menu. _(deprecated)_
- [arrowDirection](arrowdirection-swift.property.md) — The direction the arrow of the editing menu is pointing. _(deprecated)_
- [ArrowDirection](arrowdirection-swift.enum.md) — The direction the arrow of the editing menu is pointing. _(deprecated)_
