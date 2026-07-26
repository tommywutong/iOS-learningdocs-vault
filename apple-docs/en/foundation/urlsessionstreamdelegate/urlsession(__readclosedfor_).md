---
title: 'urlSession(_:readClosedFor:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessionstreamdelegate/urlsession(_:readclosedfor:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionstreamdelegate/urlsession(_:readclosedfor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionstreamdelegate/urlsession%28_%3Areadclosedfor%3A%29.json'
content_hash: 'sha256:ac1056492f578fc6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionStreamDelegate](../urlsessionstreamdelegate.md)

# urlSession(_:readClosedFor:)

<sub>Instance Method</sub>

Tells the delegate that the read side of the underlying socket has been closed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, readClosedFor streamTask: URLSessionStreamTask)
```

## Parameters

- `session` — The session containing the stream task that closed reads.

- `streamTask` — The stream task that closed reads.

## Discussion

This method may be called even if no reads are currently in progress. This method does not indicate that the stream reached end-of-file (EOF), such that no more data can be read.

## See Also

### Handling closing events

- [- URLSession:writeClosedForStreamTask:](<urlsession(__writeclosedfor_).md>) — Tells the delegate that the write side of the underlying socket has been closed.
