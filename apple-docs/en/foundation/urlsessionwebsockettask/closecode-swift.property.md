---
title: closeCode
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionwebsockettask/closecode-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionwebsockettask/closecode-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionwebsockettask/closecode-swift.property.json'
content_hash: 'sha256:9c0d89f6d52a5230'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionWebSocketTask](../urlsessionwebsockettask.md)

# closeCode

<sub>Instance Property</sub>

A code that indicates the reason a connection closed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var closeCode: URLSessionWebSocketTask.CloseCode { get }
```

## Discussion

You can retrieve the close code at any time. When the task is not yet closed, this value is [NSURLSessionWebSocketCloseCodeInvalid](closecode-swift.enum/invalid.md).

## See Also

### Closing the connection

- [- cancelWithCloseCode:reason:](<cancel(with_reason_).md>) — Sends a close frame with the given close code and optional close reason.
- [CloseCode](closecode-swift.enum.md) — A code that indicates why a WebSocket connection closed.
- [closeReason](closereason.md) — A block of data that provides further information about why a connection closed.
