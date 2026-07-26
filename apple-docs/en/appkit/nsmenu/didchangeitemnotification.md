---
title: didChangeItemNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsmenu/didchangeitemnotification
source_url: 'https://developer.apple.com/documentation/appkit/nsmenu/didchangeitemnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsmenu/didchangeitemnotification.json'
content_hash: 'sha256:1408b034779c1eaa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSMenu](../nsmenu.md)

# didChangeItemNotification

<sub>Type Property</sub>

Posted after a menu item in the menu changes appearance.

<sub>macOS</sub>

```swift
class let didChangeItemNotification: NSNotification.Name
```

## Discussion

Changes include enabling/disabling, changes in state, and changes to title. The notification object is the instance of `NSMenu` with the menu item that changed. The `userInfo` dictionary contains the following information.

| Key | Value |
|---|---|
| `@"NSMenuItemIndex"` | An `NSNumber` object containing the integer index of the menu item that changed. |

To observe this notification using Swift concurrency, use [DidChangeItemMessage](didchangeitemmessage.md).

## See Also

### Notifications

- [NSMenuDidAddItemNotification](didadditemnotification.md) — Posted after a menu item is added to the menu.
- [NSMenuDidBeginTrackingNotification](didbegintrackingnotification.md) — Posted when menu tracking begins.
- [NSMenuDidEndTrackingNotification](didendtrackingnotification.md) — Posted when menu tracking ends, even if no action is sent.
- [NSMenuDidRemoveItemNotification](didremoveitemnotification.md) — Posted after a menu item is removed from the menu.
- [NSMenuDidSendActionNotification](didsendactionnotification.md) — Posted just after the application dispatches a menu item’s action method to the menu item’s target.
- [NSMenuWillSendActionNotification](willsendactionnotification.md) — Posted just before the application dispatches a menu item’s action method to the menu item’s target.
