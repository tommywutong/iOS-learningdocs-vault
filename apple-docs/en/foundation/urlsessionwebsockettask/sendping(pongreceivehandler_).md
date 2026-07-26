---
title: 'sendPing(pongReceiveHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessionwebsockettask/sendping(pongreceivehandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionwebsockettask/sendping(pongreceivehandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionwebsockettask/sendping%28pongreceivehandler%3A%29.json'
content_hash: 'sha256:9c3979afa82db833'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionWebSocketTask](../urlsessionwebsockettask.md)

# sendPing(pongReceiveHandler:)

<sub>Instance Method</sub>

Sends a ping frame from the client side, with a closure to receive the pong from the server endpoint.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sendPing(pongReceiveHandler: @escaping @Sendable ((any Error)?) -> Void)
```

## Parameters

- `pongReceiveHandler` — A closure called by the task when it receives the pong from the server. The block/closure receives an [NSError](../nserror.md) that indicates a lost connection or other problem, or `nil` if no error occurred.

## Discussion

When sending multiple pings, the task always calls `pongReceiveHandler` in the order it sent the pings.
