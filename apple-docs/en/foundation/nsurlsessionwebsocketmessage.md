---
title: NSURLSessionWebSocketMessage
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlsessionwebsocketmessage
source_url: 'https://developer.apple.com/documentation/foundation/nsurlsessionwebsocketmessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlsessionwebsocketmessage.json'
content_hash: 'sha256:595583813d5e6ca5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSURLSessionWebSocketMessage

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@interface NSURLSessionWebSocketMessage : NSObject
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

## Topics

### Instance Properties

- [data](nsurlsessionwebsocketmessage/data.md)
- [string](nsurlsessionwebsocketmessage/string.md)
- [type](nsurlsessionwebsocketmessage/type.md)

### Instance Methods

- [initWithData:](nsurlsessionwebsocketmessage/initwithdata_.md)
- [initWithString:](nsurlsessionwebsocketmessage/initwithstring_.md)

## See Also

### Adding WebSocket tasks to a session

- [- webSocketTaskWithURL:](<urlsession/websockettask(with_)-87ipz.md>) — Creates a WebSocket task for the provided URL.
- [- webSocketTaskWithRequest:](<urlsession/websockettask(with_)-mtks.md>) — Creates a WebSocket task for the provided URL request.
- [- webSocketTaskWithURL:protocols:](<urlsession/websockettask(with_protocols_).md>) — Creates a WebSocket task given a URL and an array of protocols.
- [URLSessionWebSocketTask](urlsessionwebsockettask.md) — A URL session task that communicates over the WebSockets protocol standard.
- [URLSessionWebSocketDelegate](urlsessionwebsocketdelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to WebSocket tasks.
- [NSURLSessionWebSocketMessageType](nsurlsessionwebsocketmessagetype.md) — An enumeration of the types of messages sent and received.
