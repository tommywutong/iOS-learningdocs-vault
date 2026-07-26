---
title: 'urlSession(_:webSocketTask:didOpenWithProtocol:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessionwebsocketdelegate/urlsession(_:websockettask:didopenwithprotocol:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionwebsocketdelegate/urlsession(_:websockettask:didopenwithprotocol:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionwebsocketdelegate/urlsession%28_%3Awebsockettask%3Adidopenwithprotocol%3A%29.json'
content_hash: 'sha256:acba0e942a3c906b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionWebSocketDelegate](../urlsessionwebsocketdelegate.md)

# urlSession(_:webSocketTask:didOpenWithProtocol:)

<sub>Instance Method</sub>

Tells the delegate that the WebSocket task successfully negotiated the handshake with the endpoint, indicating the negotiated protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, webSocketTask: URLSessionWebSocketTask, didOpenWithProtocol protocol: String?)
```

## Parameters

- `session` — The session of the WebSocket task that opened.

- `webSocketTask` — The WebSocket task that opened.

- `protocol` — The protocol picked during the handshake phase. This parameter is `nil` if the server did not pick a protocol, or if the client did not advertise protocols when creating the task.

## Discussion

If the handshake fails, the task doesn’t call this delegate method.

## See Also

### Handling WebSocket lifecycle events

- [- URLSession:webSocketTask:didCloseWithCode:reason:](<urlsession(__websockettask_didclosewith_reason_).md>) — Tells the delegate that the WebSocket task received a close frame from the server endpoint, optionally including a close code and reason from the server.
