---
title: maximumMessageSize
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionwebsockettask/maximummessagesize
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionwebsockettask/maximummessagesize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionwebsockettask/maximummessagesize.json'
content_hash: 'sha256:873583de995ec5e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionWebSocketTask](../urlsessionwebsockettask.md)

# maximumMessageSize

<sub>Instance Property</sub>

The maximum number of bytes to buffer before the receive call fails with an error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var maximumMessageSize: Int { get set }
```

## Discussion

This value includes the sum of all bytes from continuation frames. Receive calls will fail once the task reaches this limit.

## See Also

### Sending and receiving data

- [send(_:completionHandler:)](<send(__completionhandler_).md>) — Sends a WebSocket message, receiving the result in a completion handler.
- [Message](message.md) — An enumeration of the types of messages sent and received.
- [receive(completionHandler:)](<receive(completionhandler_).md>) — Reads a WebSocket message once all the frames of the message are available.
