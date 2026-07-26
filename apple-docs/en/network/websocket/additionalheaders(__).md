---
title: 'additionalHeaders(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/websocket/additionalheaders(_:)'
source_url: 'https://developer.apple.com/documentation/network/websocket/additionalheaders(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/websocket/additionalheaders%28_%3A%29.json'
content_hash: 'sha256:3083e58ecda4122e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [WebSocket](../websocket.md)

# additionalHeaders(_:)

<sub>Instance Method</sub>

Set additional HTTP header fields to be sent by the client during the WebSocket handshake.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func additionalHeaders(_ headers: [(name: String, value: String)]) -> WebSocket
```

## Parameters

- `headers` — An array of HTTP header field names and values.

## Discussion

This can be used for custom protocols and cookies. Multiple headers of the same name are not allowed, and the header will replaced by the most recently set value.

> [!note] Note
> This function will only take effect on WebSocket clients.
