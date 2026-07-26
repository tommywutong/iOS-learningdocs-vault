---
title: 'setMenuVisible(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（13.0 起废弃）, iPadOS 3.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uimenucontroller/setmenuvisible(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uimenucontroller/setmenuvisible(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenucontroller/setmenuvisible%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:c0d25a781d579504'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuController](../uimenucontroller.md)

# setMenuVisible(_:animated:)

<sub>Instance Method</sub>

Shows or hides the editing menu, optionally animating the action.

> [!warning] Deprecated
> For more information, see [UIMenuController](../uimenucontroller.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func setMenuVisible(_ menuVisible: Bool, animated: Bool)
```

## Parameters

- `menuVisible` — [true](../../swift/true.md) if the menu should be shown, [false](../../swift/false.md) if it should be hidden.

- `animated` — [true](../../swift/true.md) if the showing or hiding of the menu should be animated, otherwise [false](../../swift/false.md).

## Discussion

Before showing the menu, be sure to position it relative to the selection. See [- setTargetRect:inView:](<settargetrect(__in_).md>) for details. If you do not set the target rect before displaying the menu, it appears at screen coordinates (0.0, 0.0).

## See Also

### Showing and hiding the menu

- [- showMenuFromView:rect:](<showmenu(from_rect_).md>) _(deprecated)_
- [- hideMenuFromView:](<hidemenu(from_).md>) _(deprecated)_
- [- hideMenu](<hidemenu().md>) _(deprecated)_
- [menuVisible](ismenuvisible.md) — The visibility of the editing menu. _(deprecated)_
