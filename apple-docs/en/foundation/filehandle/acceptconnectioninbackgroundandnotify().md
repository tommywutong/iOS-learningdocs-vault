---
title: acceptConnectionInBackgroundAndNotify()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filehandle/acceptconnectioninbackgroundandnotify()
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/acceptconnectioninbackgroundandnotify()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/acceptconnectioninbackgroundandnotify%28%29.json'
content_hash: 'sha256:7f2e3e484406c90e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# acceptConnectionInBackgroundAndNotify()

<sub>Instance Method</sub>

Accepts a socket connection (for stream-type sockets only) in the background and creates a file handle for the “near” (client) end of the communications channel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func acceptConnectionInBackgroundAndNotify()
```

## Discussion

This method asynchronously creates a file handle for the other end of the socket connection and returns that object by posting a [NSFileHandleConnectionAcceptedNotification](../nsnotification/name-swift.struct/nsfilehandleconnectionaccepted.md) notification in the current thread. The notification includes a `userInfo` dictionary with the created `NSFileHandle` object, which is accessible using the `NSFileHandleNotificationFileHandleItem` key.

You must call this method from a thread that has an active run loop.

### Special Considerations

The receiver must be created by an [- initWithFileDescriptor:](<init(filedescriptor_).md>) message that takes as an argument a stream-type socket created by the appropriate system routine, _and that is being listened on_. In other words, you must `bind()` the socket, and ensure that the socket has a connection backlog defined by `listen()`.

The object that will write data to the returned file handle must add itself as an observer of [NSFileHandleConnectionAcceptedNotification](../nsnotification/name-swift.struct/nsfilehandleconnectionaccepted.md).

Note that this method does not continue to listen for connection requests after it posts [NSFileHandleConnectionAcceptedNotification](../nsnotification/name-swift.struct/nsfilehandleconnectionaccepted.md). If you want to keep getting notified, you need to call [- acceptConnectionInBackgroundAndNotify](<acceptconnectioninbackgroundandnotify().md>) again in your observer method.

## See Also

### Related Documentation

- [- enqueueNotification:postingStyle:coalesceMask:forModes:](<../notificationqueue/enqueue(__postingstyle_coalescemask_formodes_).md>) — Adds a notification to the notification queue with a specified posting style, criteria for coalescing, and run loop mode.

### Reading asynchronously with notifications

- [- acceptConnectionInBackgroundAndNotifyForModes:](<acceptconnectioninbackgroundandnotify(formodes_).md>) — Accepts a socket connection (for stream-type sockets only) in the background and creates a file handle for the “near” (client) end of the communications channel.
- [- readInBackgroundAndNotify](<readinbackgroundandnotify().md>) — Reads from the file or communications channel in the background and posts a notification when finished.
- [- readInBackgroundAndNotifyForModes:](<readinbackgroundandnotify(formodes_).md>) — Reads from the file or communications channel in the background and posts a notification when finished.
- [- readToEndOfFileInBackgroundAndNotify](<readtoendoffileinbackgroundandnotify().md>) — Reads to the end of file from the file or communications channel in the background and posts a notification when finished.
- [- readToEndOfFileInBackgroundAndNotifyForModes:](<readtoendoffileinbackgroundandnotify(formodes_).md>) — Reads to the end of file from the file or communications channel in the background and posts a notification when finished.
- [- waitForDataInBackgroundAndNotify](<waitfordatainbackgroundandnotify().md>) — Asynchronously checks to see if data is available.
- [- waitForDataInBackgroundAndNotifyForModes:](<waitfordatainbackgroundandnotify(formodes_).md>) — Asynchronously checks to see if data is available.
