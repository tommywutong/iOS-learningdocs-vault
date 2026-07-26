---
title: URLSessionWebSocketTask.Message
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionwebsockettask/message
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionwebsockettask/message'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionwebsockettask/message.json'
content_hash: 'sha256:db40ce401bc81f84'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionWebSocketTask](../urlsessionwebsockettask.md)

# URLSessionWebSocketTask.Message

<sub>Enumeration</sub>

An enumeration of the types of messages sent and received.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Message
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Message types

- [URLSessionWebSocketTask.Message.data(_:)](<message/data(__).md>) — A WebSocket message that contains a block of data.
- [URLSessionWebSocketTask.Message.string(_:)](<message/string(__).md>) — A WebSocket message that contains a string.

## See Also

### Sending and receiving data

- [send(_:completionHandler:)](<send(__completionhandler_).md>) — Sends a WebSocket message, receiving the result in a completion handler.
- [receive(completionHandler:)](<receive(completionhandler_).md>) — Reads a WebSocket message once all the frames of the message are available.
- [maximumMessageSize](maximummessagesize.md) — The maximum number of bytes to buffer before the receive call fails with an error.
