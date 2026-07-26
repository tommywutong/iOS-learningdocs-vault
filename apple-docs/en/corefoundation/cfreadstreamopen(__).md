---
title: 'CFReadStreamOpen(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfreadstreamopen(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfreadstreamopen(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfreadstreamopen%28_%3A%29.json'
content_hash: 'sha256:ad4ca386deeebaac'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFReadStreamOpen(_:)

<sub>Function</sub>

Opens a stream for reading.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFReadStreamOpen(_ stream: CFReadStream!) -> Bool
```

## Parameters

- `stream` — The stream to open.

## Return Value

`TRUE` if `stream` was successfully opened, `FALSE` otherwise. If `stream` is not in the [kCFStreamStatusNotOpen](cfstreamstatus/notopen.md) state, this function returns `FALSE`.

## Discussion

Opening a stream causes it to reserve all the system resources it requires. If the stream can open in the background without blocking, this function always returns `true`. To learn when a background open operation completes, you can either schedule the stream into a run loop with [CFReadStreamScheduleWithRunLoop](<cfreadstreamschedulewithrunloop(______).md>) and wait for the stream’s client (set with [CFReadStreamSetClient](<cfreadstreamsetclient(________).md>)) to be notified or you can poll the stream using [CFReadStreamGetStatus](<cfreadstreamgetstatus(__).md>), waiting for a status of [kCFStreamStatusOpen](cfstreamstatus/open.md) or [kCFStreamStatusError](cfstreamstatus/error.md).

You do not need to wait until a stream has finished opening in the background before calling the [CFReadStreamRead](<cfreadstreamread(______).md>) function. The read operation will simply block until the open has completed.

## See Also

### Opening and Closing a Read Stream

- [CFReadStreamClose](<cfreadstreamclose(__).md>) — Closes a readable stream.
