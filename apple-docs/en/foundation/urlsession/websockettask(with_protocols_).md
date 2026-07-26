---
title: 'webSocketTask(with:protocols:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsession/websockettask(with:protocols:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/websockettask(with:protocols:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/websockettask%28with%3Aprotocols%3A%29.json'
content_hash: 'sha256:b56b8dbeb9f19d9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# webSocketTask(with:protocols:)

<sub>Instance Method</sub>

Creates a WebSocket task given a URL and an array of protocols.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func webSocketTask(with url: URL, protocols: [String]) -> URLSessionWebSocketTask
```

## Parameters

- `url` — The WebSocket URL with which to connect.

- `protocols` — An array of protocols to negotiate with the server.

## Discussion

During the WebSocket handshake, the task uses the provided protocols to negotiate a preferred protocol with the server.

> [!note] Note
> The protocol doesn’t affect the WebSocket framing. More details on the protocol are available in [RFC 6455, The WebSocket Protocol](https://tools.ietf.org/html/rfc6455).

## See Also

### Adding WebSocket tasks to a session

- [- webSocketTaskWithURL:](<websockettask(with_)-87ipz.md>) — Creates a WebSocket task for the provided URL.
- [- webSocketTaskWithRequest:](<websockettask(with_)-mtks.md>) — Creates a WebSocket task for the provided URL request.
- [URLSessionWebSocketTask](../urlsessionwebsockettask.md) — A URL session task that communicates over the WebSockets protocol standard.
- [URLSessionWebSocketDelegate](../urlsessionwebsocketdelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to WebSocket tasks.
