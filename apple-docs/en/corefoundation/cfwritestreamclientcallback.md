---
title: CFWriteStreamClientCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfwritestreamclientcallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfwritestreamclientcallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfwritestreamclientcallback.json'
content_hash: 'sha256:246a3f06749e4324'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFWriteStreamClientCallBack

<sub>Type Alias</sub>

Callback invoked when certain types of activity takes place on a writable stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFWriteStreamClientCallBack = (CFWriteStream?, CFStreamEventType, UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `stream` — The stream that experienced the event `eventType`.

- `eventType` — The event that caused the callback to be called. The possible events are listed in [CFStreamEventType](cfstreameventtype.md).

- `clientCallBackInfo` — The `info` member of the [CFStreamClientContext](cfstreamclientcontext.md) structure that was used when setting the client for `stream`.

## Discussion

This callback is called only for the events requested when setting the client with [CFWriteStreamSetClient](<cfwritestreamsetclient(________).md>).
