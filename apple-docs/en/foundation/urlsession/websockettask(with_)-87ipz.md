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
doc_path: '/documentation/foundation/urlsession/websockettask(with:)-87ipz'
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/websockettask(with:)-87ipz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/websockettask%28with%3A%29-87ipz.json'
content_hash: 'sha256:7974729278e2f776'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# webSocketTask(with:)

<sub>Instance Method</sub>

Creates a WebSocket task for the provided URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func webSocketTask(with url: URL) -> URLSessionWebSocketTask
```

## Parameters

- `url` — The WebSocket URL with which to connect.

## Discussion

The provided URL must have a `ws` or `wss` scheme.

## See Also

### Adding WebSocket tasks to a session

- [- webSocketTaskWithRequest:](<websockettask(with_)-mtks.md>) — Creates a WebSocket task for the provided URL request.
- [- webSocketTaskWithURL:protocols:](<websockettask(with_protocols_).md>) — Creates a WebSocket task given a URL and an array of protocols.
- [URLSessionWebSocketTask](../urlsessionwebsockettask.md) — A URL session task that communicates over the WebSockets protocol standard.
- [URLSessionWebSocketDelegate](../urlsessionwebsocketdelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to WebSocket tasks.
