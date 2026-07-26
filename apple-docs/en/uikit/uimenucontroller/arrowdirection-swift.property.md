---
title: arrowDirection
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+（16.0 起废弃）, iPadOS 3.2+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uimenucontroller/arrowdirection-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uimenucontroller/arrowdirection-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenucontroller/arrowdirection-swift.property.json'
content_hash: 'sha256:d33650196ff2f7ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuController](../uimenucontroller.md)

# arrowDirection

<sub>Instance Property</sub>

The direction the arrow of the editing menu is pointing.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var arrowDirection: UIMenuController.ArrowDirection { get set }
```

## Discussion

You can set the direction editing-menu arrow points by assigning a [ArrowDirection](arrowdirection-swift.enum.md) enum constant to this property. The default behavior ([UIMenuControllerArrowDefault](arrowdirection-swift.enum/default.md)) is to point up or down at the object of focus based on its location on the screen.

## See Also

### Positioning the menu

- [menuFrame](menuframe.md) — Returns the frame of the editing menu. _(deprecated)_
- [ArrowDirection](arrowdirection-swift.enum.md) — The direction the arrow of the editing menu is pointing. _(deprecated)_
- [- setTargetRect:inView:](<settargetrect(__in_).md>) — Sets the area in a view above or below which the editing menu is positioned. _(deprecated)_
