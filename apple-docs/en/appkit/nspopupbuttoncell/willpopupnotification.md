---
title: willPopUpNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nspopupbuttoncell/willpopupnotification
source_url: 'https://developer.apple.com/documentation/appkit/nspopupbuttoncell/willpopupnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nspopupbuttoncell/willpopupnotification.json'
content_hash: 'sha256:322428a549bc21f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSPopUpButtonCell](../nspopupbuttoncell.md)

# willPopUpNotification

<sub>Type Property</sub>

This notification is posted just before a pop-up menu is attached to its window frame.

<sub>macOS</sub>

```swift
class let willPopUpNotification: NSNotification.Name
```

## Discussion

You can use this notification to lazily construct your part’s menus, thus preventing unnecessary calculations until they are needed. The notification object can be either a pop-up button or its enclosed pop-up button cell. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [WillPopUpMessage](willpopupmessage.md).
