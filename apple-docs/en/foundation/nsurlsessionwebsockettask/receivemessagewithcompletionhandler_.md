---
title: 'receiveMessageWithCompletionHandler:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlsessionwebsockettask/receivemessagewithcompletionhandler:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlsessionwebsockettask/receivemessagewithcompletionhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlsessionwebsockettask/receivemessagewithcompletionhandler%3A.json'
content_hash: 'sha256:17f10da54d9095e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionWebSocketTask](../urlsessionwebsockettask.md)

# receiveMessageWithCompletionHandler:

<sub>Instance Method</sub>

Reads a WebSocket message once all the frames of the message are available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) receiveMessageWithCompletionHandler:(void (^)(NSURLSessionWebSocketMessage *message, NSError *error)) completionHandler;
```

## Parameters

- `completionHandler` — A closure that receives two parameters: the WebSocket message, and an [NSError](../nserror.md) that indicates an error encountered while receiving the message. The error is `nil` if no error occurred.

## Discussion

If the task reaches the [maximumMessageSize](../urlsessionwebsockettask/maximummessagesize.md) while buffering the frames, this call fails with an error.

## See Also

### Sending and receiving data

- [sendMessage:completionHandler:](sendmessage_completionhandler_.md) — Sends a WebSocket message, receiving the result in a completion handler.
- [maximumMessageSize](../urlsessionwebsockettask/maximummessagesize.md) — The maximum number of bytes to buffer before the receive call fails with an error.
