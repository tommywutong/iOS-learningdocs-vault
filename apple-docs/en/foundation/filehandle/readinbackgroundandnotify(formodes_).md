---
title: 'readInBackgroundAndNotify(forModes:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filehandle/readinbackgroundandnotify(formodes:)'
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/readinbackgroundandnotify(formodes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/readinbackgroundandnotify%28formodes%3A%29.json'
content_hash: 'sha256:d2a857bd45c07104'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# readInBackgroundAndNotify(forModes:)

<sub>Instance Method</sub>

Reads from the file or communications channel in the background and posts a notification when finished.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func readInBackgroundAndNotify(forModes modes: [RunLoop.Mode]?)
```

## Parameters

- `modes` — The runloop modes in which the read completion notification can be posted.

## Discussion

See [- readInBackgroundAndNotify](<readinbackgroundandnotify().md>) for details of how this method operates. This method differs from [- readInBackgroundAndNotify](<readinbackgroundandnotify().md>) in that `modes` specifies the run-loop mode (or modes) in which [NSFileHandleReadCompletionNotification](readcompletionnotification.md) can be posted.

You must call this method from a thread that has an active run loop.

## See Also

### Related Documentation

- [- enqueueNotification:postingStyle:coalesceMask:forModes:](<../notificationqueue/enqueue(__postingstyle_coalescemask_formodes_).md>) — Adds a notification to the notification queue with a specified posting style, criteria for coalescing, and run loop mode.

### Reading asynchronously with notifications

- [- acceptConnectionInBackgroundAndNotify](<acceptconnectioninbackgroundandnotify().md>) — Accepts a socket connection (for stream-type sockets only) in the background and creates a file handle for the “near” (client) end of the communications channel.
- [- acceptConnectionInBackgroundAndNotifyForModes:](<acceptconnectioninbackgroundandnotify(formodes_).md>) — Accepts a socket connection (for stream-type sockets only) in the background and creates a file handle for the “near” (client) end of the communications channel.
- [- readInBackgroundAndNotify](<readinbackgroundandnotify().md>) — Reads from the file or communications channel in the background and posts a notification when finished.
- [- readToEndOfFileInBackgroundAndNotify](<readtoendoffileinbackgroundandnotify().md>) — Reads to the end of file from the file or communications channel in the background and posts a notification when finished.
- [- readToEndOfFileInBackgroundAndNotifyForModes:](<readtoendoffileinbackgroundandnotify(formodes_).md>) — Reads to the end of file from the file or communications channel in the background and posts a notification when finished.
- [- waitForDataInBackgroundAndNotify](<waitfordatainbackgroundandnotify().md>) — Asynchronously checks to see if data is available.
- [- waitForDataInBackgroundAndNotifyForModes:](<waitfordatainbackgroundandnotify(formodes_).md>) — Asynchronously checks to see if data is available.
