---
title: waitForDataInBackgroundAndNotify()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filehandle/waitfordatainbackgroundandnotify()
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/waitfordatainbackgroundandnotify()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/waitfordatainbackgroundandnotify%28%29.json'
content_hash: 'sha256:d687af38d34a52ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# waitForDataInBackgroundAndNotify()

<sub>Instance Method</sub>

Asynchronously checks to see if data is available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func waitForDataInBackgroundAndNotify()
```

## Discussion

When the data becomes available, this method posts a [NSFileHandleDataAvailableNotification](../nsnotification/name-swift.struct/nsfilehandledataavailable.md) notification on the current thread.

You must call this method from a thread that has an active run loop.

## See Also

### Reading asynchronously with notifications

- [- acceptConnectionInBackgroundAndNotify](<acceptconnectioninbackgroundandnotify().md>) — Accepts a socket connection (for stream-type sockets only) in the background and creates a file handle for the “near” (client) end of the communications channel.
- [- acceptConnectionInBackgroundAndNotifyForModes:](<acceptconnectioninbackgroundandnotify(formodes_).md>) — Accepts a socket connection (for stream-type sockets only) in the background and creates a file handle for the “near” (client) end of the communications channel.
- [- readInBackgroundAndNotify](<readinbackgroundandnotify().md>) — Reads from the file or communications channel in the background and posts a notification when finished.
- [- readInBackgroundAndNotifyForModes:](<readinbackgroundandnotify(formodes_).md>) — Reads from the file or communications channel in the background and posts a notification when finished.
- [- readToEndOfFileInBackgroundAndNotify](<readtoendoffileinbackgroundandnotify().md>) — Reads to the end of file from the file or communications channel in the background and posts a notification when finished.
- [- readToEndOfFileInBackgroundAndNotifyForModes:](<readtoendoffileinbackgroundandnotify(formodes_).md>) — Reads to the end of file from the file or communications channel in the background and posts a notification when finished.
- [- waitForDataInBackgroundAndNotifyForModes:](<waitfordatainbackgroundandnotify(formodes_).md>) — Asynchronously checks to see if data is available.
