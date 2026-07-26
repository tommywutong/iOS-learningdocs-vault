---
title: 'webSocketTask(with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsession/websockettask(with:)-mtks'
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/websockettask(with:)-mtks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/websockettask%28with%3A%29-mtks.json'
content_hash: 'sha256:93a361336c3ce83b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# webSocketTask(with:)

<sub>Instance Method</sub>

Creates a WebSocket task for the provided URL request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func webSocketTask(with request: URLRequest) -> URLSessionWebSocketTask
```

## Parameters

- `request` — A URL request that indicates a WebSockets endpoint with which to connect.

## Discussion

You can modify the request’s properties prior to calling [- resume](<../urlsessiontask/resume().md>) on the task. The task uses these properties during the HTTP handshake phase.

To add custom protocols, add a header with the key `Sec-WebSocket-Protocol`, and a comma-separated list of protocols you want to negotiate with the server. The custom HTTP headers provided by the client remain unchanged for the handshake with the server.

## See Also

### Adding WebSocket tasks to a session

- [- webSocketTaskWithURL:](<websockettask(with_)-87ipz.md>) — Creates a WebSocket task for the provided URL.
- [- webSocketTaskWithURL:protocols:](<websockettask(with_protocols_).md>) — Creates a WebSocket task given a URL and an array of protocols.
- [URLSessionWebSocketTask](../urlsessionwebsockettask.md) — A URL session task that communicates over the WebSockets protocol standard.
- [URLSessionWebSocketDelegate](../urlsessionwebsocketdelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to WebSocket tasks.
