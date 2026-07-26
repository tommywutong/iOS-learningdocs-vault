---
title: didBeginTrackingNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsmenu/didbegintrackingnotification
source_url: 'https://developer.apple.com/documentation/appkit/nsmenu/didbegintrackingnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsmenu/didbegintrackingnotification.json'
content_hash: 'sha256:987be85cfe7f8c4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSMenu](../nsmenu.md)

# didBeginTrackingNotification

<sub>Type Property</sub>

Posted when menu tracking begins.

<sub>macOS</sub>

```swift
class let didBeginTrackingNotification: NSNotification.Name
```

## Discussion

The notification object is the main menu bar (`[NSApp mainMenu]`) or the root menu of a popup button. This notification does not contain a `userInfo` dictionary.

> [!note] Note
> This notification is available in versions 10.3 and 10.4 of macOS, however it is not publicly declared so you must declare the name constant as an `extern`, for example:
>
> ```objc
> extern NSString *NSMenuDidBeginTrackingNotification;
> ```

To observe this notification using Swift concurrency, use [DidBeginTrackingMessage](didbegintrackingmessage.md).

## See Also

### Notifications

- [NSMenuDidAddItemNotification](didadditemnotification.md) — Posted after a menu item is added to the menu.
- [NSMenuDidChangeItemNotification](didchangeitemnotification.md) — Posted after a menu item in the menu changes appearance.
- [NSMenuDidEndTrackingNotification](didendtrackingnotification.md) — Posted when menu tracking ends, even if no action is sent.
- [NSMenuDidRemoveItemNotification](didremoveitemnotification.md) — Posted after a menu item is removed from the menu.
- [NSMenuDidSendActionNotification](didsendactionnotification.md) — Posted just after the application dispatches a menu item’s action method to the menu item’s target.
- [NSMenuWillSendActionNotification](willsendactionnotification.md) — Posted just before the application dispatches a menu item’s action method to the menu item’s target.
