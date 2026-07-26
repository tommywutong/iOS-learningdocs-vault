---
title: NSFileHandleNotificationDataItem
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilehandlenotificationdataitem
source_url: 'https://developer.apple.com/documentation/foundation/nsfilehandlenotificationdataitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilehandlenotificationdataitem.json'
content_hash: 'sha256:6ac4976cca7e9b30'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSFileHandleNotificationDataItem

<sub>Global Variable</sub>

A key in the userinfo dictionary in a [NSFileHandleReadCompletionNotification](filehandle/readcompletionnotification.md) and [NSFileHandleReadToEndOfFileCompletionNotification](nsnotification/name-swift.struct/nsfilehandlereadtoendoffilecompletion.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSFileHandleNotificationDataItem: String
```

## Discussion

The corresponding value is an `NSData` object containing the available data read from a socket connection.

## See Also

### Constants

- [NSFileHandleNotificationFileHandleItem](nsfilehandlenotificationfilehandleitem.md) — A key in the userinfo dictionary in a [NSFileHandleConnectionAcceptedNotification](nsnotification/name-swift.struct/nsfilehandleconnectionaccepted.md) notification.
- [NSFileHandleNotificationMonitorModes](nsfilehandlenotificationmonitormodes.md) — Currently unused. _(deprecated)_
