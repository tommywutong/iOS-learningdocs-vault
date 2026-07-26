---
title: 'send(_:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessionwebsockettask/send(_:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionwebsockettask/send(_:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionwebsockettask/send%28_%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:234514c3965420ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionWebSocketTask](../urlsessionwebsockettask.md)

# send(_:completionHandler:)

<sub>Instance Method</sub>

Sends a WebSocket message, receiving the result in a completion handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency func send(_ message: URLSessionWebSocketTask.Message, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

## Parameters

- `message` — The WebSocket message to send to the other endpoint.

- `completionHandler` — A closure that receives an [NSError](../nserror.md) that indicates an error encountered while sending, or nil if no error occurred.

## Discussion

If an error occurs while sending the message, any outstanding work also fails.

## See Also

### Sending and receiving data

- [Message](message.md) — An enumeration of the types of messages sent and received.
- [receive(completionHandler:)](<receive(completionhandler_).md>) — Reads a WebSocket message once all the frames of the message are available.
- [maximumMessageSize](maximummessagesize.md) — The maximum number of bytes to buffer before the receive call fails with an error.
