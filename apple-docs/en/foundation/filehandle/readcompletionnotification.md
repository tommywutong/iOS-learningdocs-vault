---
title: readCompletionNotification
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filehandle/readcompletionnotification
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/readcompletionnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/readcompletionnotification.json'
content_hash: 'sha256:cfe021412f3a6b3f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# readCompletionNotification

<sub>Type Property</sub>

Posted when the file handle reads the data currently available in a file or at a communications channel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let readCompletionNotification: NSNotification.Name
```

## Discussion

It makes the data available to observers by putting it in the `userInfo` dictionary. To cause the posting of this notification, you must send either [- readInBackgroundAndNotify](<readinbackgroundandnotify().md>) or [- readInBackgroundAndNotifyForModes:](<readinbackgroundandnotify(formodes_).md>) to an appropriate `NSFileHandle` object.

The notification object is the `NSFileHandle` object that sent the notification. The `userInfo` dictionary contains the following information:

| Key | Value |
|---|---|
| `NSFileHandleNotificationDataItem` | An `NSData` object containing the available data read from a socket connection. |
| `@"NSFileHandleError"` | An `NSNumber` object containing an integer representing the UNIX-type error which occurred. |

## See Also

### Working with notifications

- [NSFileHandleConnectionAcceptedNotification](../nsnotification/name-swift.struct/nsfilehandleconnectionaccepted.md) — Posted when a file handle object establishes a socket connection between two processes, creates a file handle object for one end of the connection, and makes this object available to observers.
- [NSFileHandleDataAvailableNotification](../nsnotification/name-swift.struct/nsfilehandledataavailable.md) — Posted when the file handle determines that data is currently available for reading in a file or at a communications channel.
- [NSFileHandleReadToEndOfFileCompletionNotification](../nsnotification/name-swift.struct/nsfilehandlereadtoendoffilecompletion.md) — Posted when the file handle reads all data in the file or, in a communications channel, until the other process signals the end of data.
