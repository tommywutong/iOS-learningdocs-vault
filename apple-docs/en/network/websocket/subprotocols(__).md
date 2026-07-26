---
title: 'subprotocols(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/websocket/subprotocols(_:)'
source_url: 'https://developer.apple.com/documentation/network/websocket/subprotocols(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/websocket/subprotocols%28_%3A%29.json'
content_hash: 'sha256:e9f009989c1500b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [WebSocket](../websocket.md)

# subprotocols(_:)

<sub>Instance Method</sub>

Set the list of supported application protocols that will be presented to a WebSocket server during connection establishment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func subprotocols(_ subprotocols: [String]) -> WebSocket
```

## Parameters

- `subprotocols` — An array of subprotocol strings.

## Discussion

> [!note] Note
> This function will only take effect on WebSocket clients.
