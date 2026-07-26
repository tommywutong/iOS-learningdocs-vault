---
title: didRemoveItemNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsmenu/didremoveitemnotification
source_url: 'https://developer.apple.com/documentation/appkit/nsmenu/didremoveitemnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsmenu/didremoveitemnotification.json'
content_hash: 'sha256:fea8c7998ffa341c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSMenu](../nsmenu.md)

# didRemoveItemNotification

<sub>Type Property</sub>

Posted after a menu item is removed from the menu.

<sub>macOS</sub>

```swift
class let didRemoveItemNotification: NSNotification.Name
```

## Discussion

The notification object is the instance of `NSMenu` that just removed the menu item. The `userInfo` dictionary contains the following information.

| Key | Value |
|---|---|
| `@"NSMenuItemIndex"` | An `NSNumber` object containing the integer index of the menu item that was removed. Note that this index may no longer be valid and in any event no longer points to the menu item that was removed. |

To observe this notification using Swift concurrency, use [DidRemoveItemMessage](didremoveitemmessage.md).

## See Also

### Notifications

- [NSMenuDidAddItemNotification](didadditemnotification.md) — Posted after a menu item is added to the menu.
- [NSMenuDidChangeItemNotification](didchangeitemnotification.md) — Posted after a menu item in the menu changes appearance.
- [NSMenuDidBeginTrackingNotification](didbegintrackingnotification.md) — Posted when menu tracking begins.
- [NSMenuDidEndTrackingNotification](didendtrackingnotification.md) — Posted when menu tracking ends, even if no action is sent.
- [NSMenuDidSendActionNotification](didsendactionnotification.md) — Posted just after the application dispatches a menu item’s action method to the menu item’s target.
- [NSMenuWillSendActionNotification](willsendactionnotification.md) — Posted just before the application dispatches a menu item’s action method to the menu item’s target.
