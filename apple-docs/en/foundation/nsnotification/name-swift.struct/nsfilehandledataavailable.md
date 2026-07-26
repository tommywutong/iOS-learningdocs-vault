---
title: NSFileHandleDataAvailable
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/nsfilehandledataavailable
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsfilehandledataavailable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/nsfilehandledataavailable.json'
content_hash: 'sha256:1b750ce1ecf8b0f9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# NSFileHandleDataAvailable

<sub>Type Property</sub>

Posted when the file handle determines that data is currently available for reading in a file or at a communications channel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let NSFileHandleDataAvailable: NSNotification.Name
```

## Discussion

The observers can then issue the appropriate messages to begin reading the data. To cause the posting of this notification, you must send either [- waitForDataInBackgroundAndNotify](<../../filehandle/waitfordatainbackgroundandnotify().md>) or [- waitForDataInBackgroundAndNotifyForModes:](<../../filehandle/waitfordatainbackgroundandnotify(formodes_).md>) to an appropriate `NSFileHandle` object.

The notification object is the `NSFileHandle` object that sent the notification. This notification doesn’t contain a `userInfo` dictionary.

## See Also

### Working with notifications

- [NSFileHandleConnectionAcceptedNotification](nsfilehandleconnectionaccepted.md) — Posted when a file handle object establishes a socket connection between two processes, creates a file handle object for one end of the connection, and makes this object available to observers.
- [NSFileHandleReadCompletionNotification](../../filehandle/readcompletionnotification.md) — Posted when the file handle reads the data currently available in a file or at a communications channel.
- [NSFileHandleReadToEndOfFileCompletionNotification](nsfilehandlereadtoendoffilecompletion.md) — Posted when the file handle reads all data in the file or, in a communications channel, until the other process signals the end of data.
