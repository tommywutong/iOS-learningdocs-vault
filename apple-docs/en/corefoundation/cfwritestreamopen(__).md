---
title: 'CFWriteStreamOpen(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfwritestreamopen(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfwritestreamopen(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfwritestreamopen%28_%3A%29.json'
content_hash: 'sha256:47dbc423749becff'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFWriteStreamOpen(_:)

<sub>Function</sub>

Opens a stream for writing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFWriteStreamOpen(_ stream: CFWriteStream!) -> Bool
```

## Parameters

- `stream` — The stream to open.

## Return Value

`true` if `stream` was successfully opened, `false` otherwise. If `stream` is not in the [kCFStreamStatusNotOpen](cfstreamstatus/notopen.md) state, this function returns `false`.

## Discussion

Opening a stream causes it to reserve all the system resources it requires. If the stream can open in the background without blocking, this function always returns `true`. To learn when a background open operation completes, you can either schedule the stream into a run loop with [CFWriteStreamScheduleWithRunLoop](<cfwritestreamschedulewithrunloop(______).md>) and wait for the stream’s client (set with [CFWriteStreamSetClient](<cfwritestreamsetclient(________).md>)) to be notified or you can poll the stream using [CFWriteStreamGetStatus](<cfwritestreamgetstatus(__).md>), waiting for a status of [kCFStreamStatusOpen](cfstreamstatus/open.md) or [kCFStreamStatusError](cfstreamstatus/error.md).

## See Also

### Opening and Closing a Stream

- [CFWriteStreamClose](<cfwritestreamclose(__).md>) — Closes a writable stream.
