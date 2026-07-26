---
title: NSFileHandleNotificationFileHandleItem
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilehandlenotificationfilehandleitem
source_url: 'https://developer.apple.com/documentation/foundation/nsfilehandlenotificationfilehandleitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilehandlenotificationfilehandleitem.json'
content_hash: 'sha256:56ed1a1dc9416e18'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSFileHandleNotificationFileHandleItem

<sub>Global Variable</sub>

A key in the userinfo dictionary in a [NSFileHandleConnectionAcceptedNotification](nsnotification/name-swift.struct/nsfilehandleconnectionaccepted.md) notification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSFileHandleNotificationFileHandleItem: String
```

## Discussion

The corresponding value is the `NSFileHandle` object representing the “near” end of a socket connection.

## See Also

### Constants

- [NSFileHandleNotificationDataItem](nsfilehandlenotificationdataitem.md) — A key in the userinfo dictionary in a [NSFileHandleReadCompletionNotification](filehandle/readcompletionnotification.md) and [NSFileHandleReadToEndOfFileCompletionNotification](nsnotification/name-swift.struct/nsfilehandlereadtoendoffilecompletion.md).
- [NSFileHandleNotificationMonitorModes](nsfilehandlenotificationmonitormodes.md) — Currently unused. _(deprecated)_
