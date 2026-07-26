---
title: contextHelpModeDidDeactivateNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nshelpmanager/contexthelpmodediddeactivatenotification
source_url: 'https://developer.apple.com/documentation/appkit/nshelpmanager/contexthelpmodediddeactivatenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nshelpmanager/contexthelpmodediddeactivatenotification.json'
content_hash: 'sha256:a92e9fb540f2ffb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSHelpManager](../nshelpmanager.md)

# contextHelpModeDidDeactivateNotification

<sub>Type Property</sub>

Posted when the application exits context-sensitive help mode. This happens when the user clicks the mouse button while the cursor is anywhere on the screen after displaying a context-sensitive help topic.

<sub>macOS</sub>

```swift
class let contextHelpModeDidDeactivateNotification: NSNotification.Name
```

## Discussion

The notification object is the help manager. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [ContextHelpModeDidDeactivateMessage](contexthelpmodediddeactivatemessage.md).

## See Also

### Notifications

- [NSContextHelpModeDidActivateNotification](contexthelpmodedidactivatenotification.md) — Posted when the application enters context-sensitive help mode. This typically happens when the user holds down the Help key.
