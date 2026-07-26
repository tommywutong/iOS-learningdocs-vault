---
title: CFUserNotificationCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfusernotificationcallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfusernotificationcallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfusernotificationcallback.json'
content_hash: 'sha256:887d94e8e87961fe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFUserNotificationCallBack

<sub>Type Alias</sub>

Callback invoked when an asynchronous user notification dialog is dismissed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFUserNotificationCallBack = (CFUserNotification?, CFOptionFlags) -> Void
```

## Parameters

- `userNotification` — The user notification that was dismissed.

- `responseFlags` — On return, contains flags identifying how the notification was dismissed, the state of any checkboxes, and the selected item of the pop-up menu. See [CFUserNotificationReceiveResponse](<cfusernotificationreceiveresponse(______).md>) for details.
