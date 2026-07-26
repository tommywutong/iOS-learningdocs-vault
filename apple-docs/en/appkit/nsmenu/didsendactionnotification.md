---
title: didSendActionNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsmenu/didsendactionnotification
source_url: 'https://developer.apple.com/documentation/appkit/nsmenu/didsendactionnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsmenu/didsendactionnotification.json'
content_hash: 'sha256:75b43fb182eb2664'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSMenu](../nsmenu.md)

# didSendActionNotification

<sub>Type Property</sub>

Posted just after the application dispatches a menu item’s action method to the menu item’s target.

<sub>macOS</sub>

```swift
class let didSendActionNotification: NSNotification.Name
```

## Discussion

The notification object is the instance of `NSMenu` containing the chosen menu item. The `userInfo` dictionary contains the following information.

| Key | Value |
|---|---|
| `@"MenuItem"` | The menu item that was chosen. |

To observe this notification using Swift concurrency, use [DidSendActionMessage](didsendactionmessage.md).

## See Also

### Notifications

- [NSMenuDidAddItemNotification](didadditemnotification.md) — Posted after a menu item is added to the menu.
- [NSMenuDidChangeItemNotification](didchangeitemnotification.md) — Posted after a menu item in the menu changes appearance.
- [NSMenuDidBeginTrackingNotification](didbegintrackingnotification.md) — Posted when menu tracking begins.
- [NSMenuDidEndTrackingNotification](didendtrackingnotification.md) — Posted when menu tracking ends, even if no action is sent.
- [NSMenuDidRemoveItemNotification](didremoveitemnotification.md) — Posted after a menu item is removed from the menu.
- [NSMenuWillSendActionNotification](willsendactionnotification.md) — Posted just before the application dispatches a menu item’s action method to the menu item’s target.
