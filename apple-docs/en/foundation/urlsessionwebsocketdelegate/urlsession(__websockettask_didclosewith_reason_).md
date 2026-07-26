---
title: 'urlSession(_:webSocketTask:didCloseWith:reason:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessionwebsocketdelegate/urlsession(_:websockettask:didclosewith:reason:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionwebsocketdelegate/urlsession(_:websockettask:didclosewith:reason:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionwebsocketdelegate/urlsession%28_%3Awebsockettask%3Adidclosewith%3Areason%3A%29.json'
content_hash: 'sha256:2a1d323e9d197d2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionWebSocketDelegate](../urlsessionwebsocketdelegate.md)

# urlSession(_:webSocketTask:didCloseWith:reason:)

<sub>Instance Method</sub>

Tells the delegate that the WebSocket task received a close frame from the server endpoint, optionally including a close code and reason from the server.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, webSocketTask: URLSessionWebSocketTask, didCloseWith closeCode: URLSessionWebSocketTask.CloseCode, reason: Data?)
```

## Parameters

- `session` — The session of the WebSocket task that closed.

- `webSocketTask` — The WebSocket task that closed.

- `closeCode` — The close code provided by the server. If the close frame didn’t include a close code, this value is `nil`.

- `reason` — The close reason provided by the server. If the close frame didn’t include a reason, this value is `nil`.

## See Also

### Handling WebSocket lifecycle events

- [- URLSession:webSocketTask:didOpenWithProtocol:](<urlsession(__websockettask_didopenwithprotocol_).md>) — Tells the delegate that the WebSocket task successfully negotiated the handshake with the endpoint, indicating the negotiated protocol.
