---
title: URLSessionWebSocketDelegate
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionwebsocketdelegate
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionwebsocketdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionwebsocketdelegate.json'
content_hash: 'sha256:7f5877485e1e9067'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLSessionWebSocketDelegate

<sub>Protocol</sub>

A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to WebSocket tasks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol URLSessionWebSocketDelegate : URLSessionTaskDelegate
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [URLSessionDelegate](urlsessiondelegate.md), [URLSessionTaskDelegate](urlsessiontaskdelegate.md)

## Topics

### Handling WebSocket lifecycle events

- [- URLSession:webSocketTask:didOpenWithProtocol:](<urlsessionwebsocketdelegate/urlsession(__websockettask_didopenwithprotocol_).md>) — Tells the delegate that the WebSocket task successfully negotiated the handshake with the endpoint, indicating the negotiated protocol.
- [- URLSession:webSocketTask:didCloseWithCode:reason:](<urlsessionwebsocketdelegate/urlsession(__websockettask_didclosewith_reason_).md>) — Tells the delegate that the WebSocket task received a close frame from the server endpoint, optionally including a close code and reason from the server.

## See Also

### Adding WebSocket tasks to a session

- [- webSocketTaskWithURL:](<urlsession/websockettask(with_)-87ipz.md>) — Creates a WebSocket task for the provided URL.
- [- webSocketTaskWithRequest:](<urlsession/websockettask(with_)-mtks.md>) — Creates a WebSocket task for the provided URL request.
- [- webSocketTaskWithURL:protocols:](<urlsession/websockettask(with_protocols_).md>) — Creates a WebSocket task given a URL and an array of protocols.
- [URLSessionWebSocketTask](urlsessionwebsockettask.md) — A URL session task that communicates over the WebSockets protocol standard.
