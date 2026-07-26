---
title: contextHelpModeDidActivateNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nshelpmanager/contexthelpmodedidactivatenotification
source_url: 'https://developer.apple.com/documentation/appkit/nshelpmanager/contexthelpmodedidactivatenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nshelpmanager/contexthelpmodedidactivatenotification.json'
content_hash: 'sha256:d1f606d88cc54d9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSHelpManager](../nshelpmanager.md)

# contextHelpModeDidActivateNotification

<sub>Type Property</sub>

Posted when the application enters context-sensitive help mode. This typically happens when the user holds down the Help key.

<sub>macOS</sub>

```swift
class let contextHelpModeDidActivateNotification: NSNotification.Name
```

## Discussion

The notification object is the help manager. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [ContextHelpModeDidActivateMessage](contexthelpmodedidactivatemessage.md).

## See Also

### Notifications

- [NSContextHelpModeDidDeactivateNotification](contexthelpmodediddeactivatenotification.md) — Posted when the application exits context-sensitive help mode. This happens when the user clicks the mouse button while the cursor is anywhere on the screen after displaying a context-sensitive help topic.
