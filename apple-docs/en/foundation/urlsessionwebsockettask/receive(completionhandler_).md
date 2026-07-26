---
title: 'receive(completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessionwebsockettask/receive(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionwebsockettask/receive(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionwebsockettask/receive%28completionhandler%3A%29.json'
content_hash: 'sha256:19ff67faca13fc80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionWebSocketTask](../urlsessionwebsockettask.md)

# receive(completionHandler:)

<sub>Instance Method</sub>

Reads a WebSocket message once all the frames of the message are available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency func receive(completionHandler: @escaping @Sendable (Result<URLSessionWebSocketTask.Message, any Error>) -> Void)
```

## Parameters

- `completionHandler` — A closure that receives two parameters: the WebSocket message, and an [NSError](../nserror.md) that indicates an error encountered while receiving the message. The error is `nil` if no error occurred.

## Discussion

If the task reaches the [maximumMessageSize](maximummessagesize.md) while buffering the frames, this call fails with an error.

## See Also

### Sending and receiving data

- [send(_:completionHandler:)](<send(__completionhandler_).md>) — Sends a WebSocket message, receiving the result in a completion handler.
- [Message](message.md) — An enumeration of the types of messages sent and received.
- [maximumMessageSize](maximummessagesize.md) — The maximum number of bytes to buffer before the receive call fails with an error.
