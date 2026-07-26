---
title: URLSessionWebSocketTask
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionwebsockettask
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionwebsockettask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionwebsockettask.json'
content_hash: 'sha256:5e119fc211ad187a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLSessionWebSocketTask

<sub>Class</sub>

A URL session task that communicates over the WebSockets protocol standard.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class URLSessionWebSocketTask
```

## Overview

[URLSessionWebSocketTask](urlsessionwebsockettask.md) is a concrete subclass of [URLSessionTask](urlsessiontask.md) that provides a message-oriented transport protocol over TCP and TLS in the form of WebSocket framing. It follows the WebSocket Protocol defined in [RFC 6455](https://tools.ietf.org/html/rfc6455).

You create a [URLSessionWebSocketTask](urlsessionwebsockettask.md) with either a `ws:` or `wss:` URL. When creating the task, you can also provide a list of protocols to advertise during the handshake phase. Once the handshake completes, your app receives notifications through the session’s [delegate](urlsession/delegate.md).

You send data with [send(_:completionHandler:)](<urlsessionwebsockettask/send(__completionhandler_).md>) and receive data with [receive(completionHandler:)](<urlsessionwebsockettask/receive(completionhandler_).md>). The task performs reads and writes asynchronously, and allows you to send and receive messages that contain both binary frames and UTF-8 encoded text frames. The task enqueues any reads or writes you perform prior to the handshake’s completion, and executes them after the handshake completes.

[URLSessionWebSocketTask](urlsessionwebsockettask.md) supports redirection and authentication like other types of tasks do, using the methods in [URLSessionTaskDelegate](urlsessiontaskdelegate.md). The WebSocket task calls the redirection and authentication delegate methods prior to completing the handshake. The WebSocket task also supports cookies, by storing cookies to the session configuration’s [HTTPCookieStorage](urlsessionconfiguration/httpcookiestorage.md), and attaches cookies to outgoing HTTP handshake requests.

> [!note] Note
> watchOS supports [URLSessionWebSocketTask](urlsessionwebsockettask.md) for specific use cases. For more details, see [TN3135: Low-level networking on watchOS](../technotes/tn3135-low-level-networking-on-watchos.md).

## Relationships

- **Inherits From**: [URLSessionTask](urlsessiontask.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [ProgressReporting](progressreporting.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Sending and receiving data

- [send(_:completionHandler:)](<urlsessionwebsockettask/send(__completionhandler_).md>) — Sends a WebSocket message, receiving the result in a completion handler.
- [Message](urlsessionwebsockettask/message.md) — An enumeration of the types of messages sent and received.
- [receive(completionHandler:)](<urlsessionwebsockettask/receive(completionhandler_).md>) — Reads a WebSocket message once all the frames of the message are available.
- [maximumMessageSize](urlsessionwebsockettask/maximummessagesize.md) — The maximum number of bytes to buffer before the receive call fails with an error.

### Sending ping frames

- [- sendPingWithPongReceiveHandler:](<urlsessionwebsockettask/sendping(pongreceivehandler_).md>) — Sends a ping frame from the client side, with a closure to receive the pong from the server endpoint.

### Closing the connection

- [- cancelWithCloseCode:reason:](<urlsessionwebsockettask/cancel(with_reason_).md>) — Sends a close frame with the given close code and optional close reason.
- [closeCode](urlsessionwebsockettask/closecode-swift.property.md) — A code that indicates the reason a connection closed.
- [CloseCode](urlsessionwebsockettask/closecode-swift.enum.md) — A code that indicates why a WebSocket connection closed.
- [closeReason](urlsessionwebsockettask/closereason.md) — A block of data that provides further information about why a connection closed.

### Instance Methods

- [receive()](<urlsessionwebsockettask/receive().md>)
- [send(_:)](<urlsessionwebsockettask/send(__).md>)

## See Also

### Adding WebSocket tasks to a session

- [- webSocketTaskWithURL:](<urlsession/websockettask(with_)-87ipz.md>) — Creates a WebSocket task for the provided URL.
- [- webSocketTaskWithRequest:](<urlsession/websockettask(with_)-mtks.md>) — Creates a WebSocket task for the provided URL request.
- [- webSocketTaskWithURL:protocols:](<urlsession/websockettask(with_protocols_).md>) — Creates a WebSocket task given a URL and an array of protocols.
- [URLSessionWebSocketDelegate](urlsessionwebsocketdelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to WebSocket tasks.
