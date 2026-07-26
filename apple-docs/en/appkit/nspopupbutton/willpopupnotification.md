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
doc_path: /documentation/appkit/nspopupbutton/willpopupnotification
source_url: 'https://developer.apple.com/documentation/appkit/nspopupbutton/willpopupnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nspopupbutton/willpopupnotification.json'
content_hash: 'sha256:9e8490ac842cea04'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSPopUpButton](../nspopupbutton.md)

# willPopUpNotification

<sub>Type Property</sub>

Posted when an `NSPopUpButton` object receives a mouse-down event—that is, when the user is about to select an item from the menu.

<sub>macOS</sub>

```swift
class let willPopUpNotification: NSNotification.Name
```

## Discussion

The notification object is the selected `NSPopUpButton` object. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [WillPopUpMessage](willpopupmessage.md).
