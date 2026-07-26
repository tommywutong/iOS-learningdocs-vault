---
title: NSFileHandleConnectionAccepted
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/nsfilehandleconnectionaccepted
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsfilehandleconnectionaccepted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/nsfilehandleconnectionaccepted.json'
content_hash: 'sha256:4f3e8f118f0435a8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# NSFileHandleConnectionAccepted

<sub>Type Property</sub>

Posted when a file handle object establishes a socket connection between two processes, creates a file handle object for one end of the connection, and makes this object available to observers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let NSFileHandleConnectionAccepted: NSNotification.Name
```

## Discussion

To cause the posting of this notification, you must send either [- acceptConnectionInBackgroundAndNotify](<../../filehandle/acceptconnectioninbackgroundandnotify().md>) or [- acceptConnectionInBackgroundAndNotifyForModes:](<../../filehandle/acceptconnectioninbackgroundandnotify(formodes_).md>) to an `NSFileHandle` object representing a server stream-type socket.

The notification object is the `NSFileHandle` object that sent the notification. The `userInfo` dictionary contains the following information:

| Key | Value |
|---|---|
| `NSFileHandleNotificationFileHandleItem` | The `NSFileHandle` object representing the “near” end of a socket connection. |
| `@"NSFileHandleError"` | An `NSNumber` object containing an integer representing the UNIX-type error which occurred. |

## See Also

### Working with notifications

- [NSFileHandleDataAvailableNotification](nsfilehandledataavailable.md) — Posted when the file handle determines that data is currently available for reading in a file or at a communications channel.
- [NSFileHandleReadCompletionNotification](../../filehandle/readcompletionnotification.md) — Posted when the file handle reads the data currently available in a file or at a communications channel.
- [NSFileHandleReadToEndOfFileCompletionNotification](nsfilehandlereadtoendoffilecompletion.md) — Posted when the file handle reads all data in the file or, in a communications channel, until the other process signals the end of data.
