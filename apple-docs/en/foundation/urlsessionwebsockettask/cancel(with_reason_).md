---
title: 'cancel(with:reason:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessionwebsockettask/cancel(with:reason:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionwebsockettask/cancel(with:reason:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionwebsockettask/cancel%28with%3Areason%3A%29.json'
content_hash: 'sha256:41f10fde9cf9302b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionWebSocketTask](../urlsessionwebsockettask.md)

# cancel(with:reason:)

<sub>Instance Method</sub>

Sends a close frame with the given close code and optional close reason.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancel(with closeCode: URLSessionWebSocketTask.CloseCode, reason: Data?)
```

## Parameters

- `closeCode` — A [CloseCode](closecode-swift.enum.md) that indicates the reason for closing the connection.

- `reason` — Optional further information to explain the closing. The value of this parameter is defined by the endpoints, not by the standard.

## Discussion

If you call [- cancel](<../urlsessiontask/cancel().md>) on the task instead of this method, it sends a cancellation frame with no close code or reason.

## See Also

### Closing the connection

- [closeCode](closecode-swift.property.md) — A code that indicates the reason a connection closed.
- [CloseCode](closecode-swift.enum.md) — A code that indicates why a WebSocket connection closed.
- [closeReason](closereason.md) — A block of data that provides further information about why a connection closed.
