---
title: closeReason
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionwebsockettask/closereason
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionwebsockettask/closereason'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionwebsockettask/closereason.json'
content_hash: 'sha256:289c24601a224f88'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionWebSocketTask](../urlsessionwebsockettask.md)

# closeReason

<sub>Instance Property</sub>

A block of data that provides further information about why a connection closed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var closeReason: Data? { get }
```

## Discussion

The close reason provides further information about why a connection closed, beyond that provided by the [closeCode](closecode-swift.property.md). The value of this property isn’t defined by [RFC 6455](https://tools.ietf.org/html/rfc6455); the endpoints define how it’s used.

You can retrieve the close reason at any time. When the task is not yet closed, this value is [NSURLSessionWebSocketCloseCodeInvalid](closecode-swift.enum/invalid.md).

## See Also

### Closing the connection

- [- cancelWithCloseCode:reason:](<cancel(with_reason_).md>) — Sends a close frame with the given close code and optional close reason.
- [closeCode](closecode-swift.property.md) — A code that indicates the reason a connection closed.
- [CloseCode](closecode-swift.enum.md) — A code that indicates why a WebSocket connection closed.
