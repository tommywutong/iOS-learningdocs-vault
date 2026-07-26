---
title: willHideMenuNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+（16.0 起废弃）, iPadOS 3.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uimenucontroller/willhidemenunotification
source_url: 'https://developer.apple.com/documentation/uikit/uimenucontroller/willhidemenunotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenucontroller/willhidemenunotification.json'
content_hash: 'sha256:d0495d482f7c98e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuController](../uimenucontroller.md)

# willHideMenuNotification

<sub>Type Property</sub>

Posted by the menu controller just before it hides the menu.

> [!warning] Deprecated
> Use [UIEditMenuInteraction](../uieditmenuinteraction.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated class let willHideMenuNotification: NSNotification.Name
```

## Discussion

There is no `userInfo` dictionary.

## See Also

### Notifications

- [UIMenuControllerWillShowMenuNotification](willshowmenunotification.md) — Posted by the menu controller just before it shows the menu. _(deprecated)_
- [UIMenuControllerDidShowMenuNotification](didshowmenunotification.md) — Posted by the menu controller just after it shows the menu. _(deprecated)_
- [UIMenuControllerDidHideMenuNotification](didhidemenunotification.md) — Posted by the menu controller just after it hides the menu. _(deprecated)_
- [UIMenuControllerMenuFrameDidChangeNotification](menuframedidchangenotification.md) — Posted when the frame of a visible menu changes. _(deprecated)_
