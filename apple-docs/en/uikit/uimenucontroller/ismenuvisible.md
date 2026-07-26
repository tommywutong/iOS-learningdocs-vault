---
title: isMenuVisible
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（16.0 起废弃）, iPadOS 3.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uimenucontroller/ismenuvisible
source_url: 'https://developer.apple.com/documentation/uikit/uimenucontroller/ismenuvisible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenucontroller/ismenuvisible.json'
content_hash: 'sha256:3cab34683fea8b10'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuController](../uimenucontroller.md)

# isMenuVisible

<sub>Instance Property</sub>

The visibility of the editing menu.

> [!warning] Deprecated
> For more information, see [UIMenuController](../uimenucontroller.md).

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var isMenuVisible: Bool { get set }
```

## Discussion

Setting this property displays or hides the menu immediately, without animation. For animating the showing or hiding of the menu, use the [- setMenuVisible:animated:](<setmenuvisible(__animated_).md>) method. Before showing the menu, be sure to position it relative to the selection.

## See Also

### Showing and hiding the menu

- [- showMenuFromView:rect:](<showmenu(from_rect_).md>) _(deprecated)_
- [- hideMenuFromView:](<hidemenu(from_).md>) _(deprecated)_
- [- hideMenu](<hidemenu().md>) _(deprecated)_
- [- setMenuVisible:animated:](<setmenuvisible(__animated_).md>) — Shows or hides the editing menu, optionally animating the action. _(deprecated)_
