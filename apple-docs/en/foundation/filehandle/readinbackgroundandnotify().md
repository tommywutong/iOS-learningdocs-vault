---
title: readInBackgroundAndNotify()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filehandle/readinbackgroundandnotify()
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/readinbackgroundandnotify()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/readinbackgroundandnotify%28%29.json'
content_hash: 'sha256:fbe6726583cbbdeb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# readInBackgroundAndNotify()

<sub>Instance Method</sub>

Reads from the file or communications channel in the background and posts a notification when finished.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func readInBackgroundAndNotify()
```

## Discussion

This method performs an asynchronous [availableData](availabledata.md) operation on a file or communications channel and posts an [NSFileHandleReadCompletionNotification](readcompletionnotification.md) notification on the current thread when that operation is complete. You must call this method from a thread that has an active run loop.

The length of the data is limited to the buffer size of the underlying operating system. The notification includes a `userInfo` dictionary that contains the data read; access this object using the `NSFileHandleNotificationDataItem` key.

Any object interested in receiving this data asynchronously must add itself as an observer of [NSFileHandleReadCompletionNotification](readcompletionnotification.md). In communication via stream-type sockets, the receiver is often the object returned in the `userInfo` dictionary of [NSFileHandleConnectionAcceptedNotification](../nsnotification/name-swift.struct/nsfilehandleconnectionaccepted.md).

Note that this method does not cause a continuous stream of notifications to be sent. If you wish to keep getting notified, you’ll also need to call [- readInBackgroundAndNotify](<readinbackgroundandnotify().md>) in your observer method.

## See Also

### Related Documentation

- [- enqueueNotification:postingStyle:coalesceMask:forModes:](<../notificationqueue/enqueue(__postingstyle_coalescemask_formodes_).md>) — Adds a notification to the notification queue with a specified posting style, criteria for coalescing, and run loop mode.

### Reading asynchronously with notifications

- [- acceptConnectionInBackgroundAndNotify](<acceptconnectioninbackgroundandnotify().md>) — Accepts a socket connection (for stream-type sockets only) in the background and creates a file handle for the “near” (client) end of the communications channel.
- [- acceptConnectionInBackgroundAndNotifyForModes:](<acceptconnectioninbackgroundandnotify(formodes_).md>) — Accepts a socket connection (for stream-type sockets only) in the background and creates a file handle for the “near” (client) end of the communications channel.
- [- readInBackgroundAndNotifyForModes:](<readinbackgroundandnotify(formodes_).md>) — Reads from the file or communications channel in the background and posts a notification when finished.
- [- readToEndOfFileInBackgroundAndNotify](<readtoendoffileinbackgroundandnotify().md>) — Reads to the end of file from the file or communications channel in the background and posts a notification when finished.
- [- readToEndOfFileInBackgroundAndNotifyForModes:](<readtoendoffileinbackgroundandnotify(formodes_).md>) — Reads to the end of file from the file or communications channel in the background and posts a notification when finished.
- [- waitForDataInBackgroundAndNotify](<waitfordatainbackgroundandnotify().md>) — Asynchronously checks to see if data is available.
- [- waitForDataInBackgroundAndNotifyForModes:](<waitfordatainbackgroundandnotify(formodes_).md>) — Asynchronously checks to see if data is available.
