---
title: 'sendMessage:completionHandler:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlsessionwebsockettask/sendmessage:completionhandler:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlsessionwebsockettask/sendmessage:completionhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlsessionwebsockettask/sendmessage%3Acompletionhandler%3A.json'
content_hash: 'sha256:83d1c0513f2584b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionWebSocketTask](../urlsessionwebsockettask.md)

# sendMessage:completionHandler:

<sub>Instance Method</sub>

Sends a WebSocket message, receiving the result in a completion handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) sendMessage:(NSURLSessionWebSocketMessage *) message completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Parameters

- `message` — The WebSocket message to send.

- `completionHandler` — A block that receives an [NSError](../nserror.md) that indicates an error encountered while sending, or `nil` if no error occurred.

## Discussion

If an error occurs while sending the message, any outstanding work also fails.

## See Also

### Sending and receiving data

- [receiveMessageWithCompletionHandler:](receivemessagewithcompletionhandler_.md) — Reads a WebSocket message once all the frames of the message are available.
- [maximumMessageSize](../urlsessionwebsockettask/maximummessagesize.md) — The maximum number of bytes to buffer before the receive call fails with an error.
