---
title: didAddItemNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsmenu/didadditemnotification
source_url: 'https://developer.apple.com/documentation/appkit/nsmenu/didadditemnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsmenu/didadditemnotification.json'
content_hash: 'sha256:beb09aa6d528b4cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSMenu](../nsmenu.md)

# didAddItemNotification

<sub>Type Property</sub>

Posted after a menu item is added to the menu.

<sub>macOS</sub>

```swift
class let didAddItemNotification: NSNotification.Name
```

## Discussion

The notification object is the instance of `NSMenu` that just added the new menu item. The `userInfo` dictionary contains the following information.

| Key | Value |
|---|---|
| `@"NSMenuItemIndex"` | An `NSNumber` object containing the integer index of the menu item that was added. |

To observe this notification using Swift concurrency, use [DidAddItemMessage](didadditemmessage.md).

## See Also

### Notifications

- [NSMenuDidChangeItemNotification](didchangeitemnotification.md) — Posted after a menu item in the menu changes appearance.
- [NSMenuDidBeginTrackingNotification](didbegintrackingnotification.md) — Posted when menu tracking begins.
- [NSMenuDidEndTrackingNotification](didendtrackingnotification.md) — Posted when menu tracking ends, even if no action is sent.
- [NSMenuDidRemoveItemNotification](didremoveitemnotification.md) — Posted after a menu item is removed from the menu.
- [NSMenuDidSendActionNotification](didsendactionnotification.md) — Posted just after the application dispatches a menu item’s action method to the menu item’s target.
- [NSMenuWillSendActionNotification](willsendactionnotification.md) — Posted just before the application dispatches a menu item’s action method to the menu item’s target.
