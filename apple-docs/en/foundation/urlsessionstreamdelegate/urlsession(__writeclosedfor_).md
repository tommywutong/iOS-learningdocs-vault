---
title: 'urlSession(_:writeClosedFor:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessionstreamdelegate/urlsession(_:writeclosedfor:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionstreamdelegate/urlsession(_:writeclosedfor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionstreamdelegate/urlsession%28_%3Awriteclosedfor%3A%29.json'
content_hash: 'sha256:306bd84c322a160b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionStreamDelegate](../urlsessionstreamdelegate.md)

# urlSession(_:writeClosedFor:)

<sub>Instance Method</sub>

Tells the delegate that the write side of the underlying socket has been closed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, writeClosedFor streamTask: URLSessionStreamTask)
```

## Parameters

- `session` — The session containing the stream task that closed writes.

- `streamTask` — The stream task that closed writes.

## Discussion

This method may be called even if no writes are currently in progress.

## See Also

### Handling closing events

- [- URLSession:readClosedForStreamTask:](<urlsession(__readclosedfor_).md>) — Tells the delegate that the read side of the underlying socket has been closed.
