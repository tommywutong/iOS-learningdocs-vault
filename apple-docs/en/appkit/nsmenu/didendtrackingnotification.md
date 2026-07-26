---
title: didEndTrackingNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsmenu/didendtrackingnotification
source_url: 'https://developer.apple.com/documentation/appkit/nsmenu/didendtrackingnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsmenu/didendtrackingnotification.json'
content_hash: 'sha256:3e23272830d7be6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSMenu](../nsmenu.md)

# didEndTrackingNotification

<sub>Type Property</sub>

Posted when menu tracking ends, even if no action is sent.

<sub>macOS</sub>

```swift
class let didEndTrackingNotification: NSNotification.Name
```

## Discussion

The notification object is the main menu bar (`[NSApp mainMenu]`) or the root menu of a popup button. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [DidEndTrackingMessage](didendtrackingmessage.md).

## See Also

### Notifications

- [NSMenuDidAddItemNotification](didadditemnotification.md) — Posted after a menu item is added to the menu.
- [NSMenuDidChangeItemNotification](didchangeitemnotification.md) — Posted after a menu item in the menu changes appearance.
- [NSMenuDidBeginTrackingNotification](didbegintrackingnotification.md) — Posted when menu tracking begins.
- [NSMenuDidRemoveItemNotification](didremoveitemnotification.md) — Posted after a menu item is removed from the menu.
- [NSMenuDidSendActionNotification](didsendactionnotification.md) — Posted just after the application dispatches a menu item’s action method to the menu item’s target.
- [NSMenuWillSendActionNotification](willsendactionnotification.md) — Posted just before the application dispatches a menu item’s action method to the menu item’s target.
