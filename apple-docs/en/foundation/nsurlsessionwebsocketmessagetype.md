---
title: NSURLSessionWebSocketMessageType
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlsessionwebsocketmessagetype
source_url: 'https://developer.apple.com/documentation/foundation/nsurlsessionwebsocketmessagetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlsessionwebsocketmessagetype.json'
content_hash: 'sha256:8aa9c5e7c659ac69'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSURLSessionWebSocketMessageType

<sub>Enumeration</sub>

An enumeration of the types of messages sent and received.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
enum NSURLSessionWebSocketMessageType : NSInteger;
```

## Topics

### Enumeration Cases

- [NSURLSessionWebSocketMessageTypeData](nsurlsessionwebsocketmessagetype/nsurlsessionwebsocketmessagetypedata.md)
- [NSURLSessionWebSocketMessageTypeString](nsurlsessionwebsocketmessagetype/nsurlsessionwebsocketmessagetypestring.md)

## See Also

### Adding WebSocket tasks to a session

- [- webSocketTaskWithURL:](<urlsession/websockettask(with_)-87ipz.md>) — Creates a WebSocket task for the provided URL.
- [- webSocketTaskWithRequest:](<urlsession/websockettask(with_)-mtks.md>) — Creates a WebSocket task for the provided URL request.
- [- webSocketTaskWithURL:protocols:](<urlsession/websockettask(with_protocols_).md>) — Creates a WebSocket task given a URL and an array of protocols.
- [URLSessionWebSocketTask](urlsessionwebsockettask.md) — A URL session task that communicates over the WebSockets protocol standard.
- [URLSessionWebSocketDelegate](urlsessionwebsocketdelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to WebSocket tasks.
- [NSURLSessionWebSocketMessage](nsurlsessionwebsocketmessage.md)
