---
title: 'maximumMessageSize(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/websocket/maximummessagesize(_:)'
source_url: 'https://developer.apple.com/documentation/network/websocket/maximummessagesize(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/websocket/maximummessagesize%28_%3A%29.json'
content_hash: 'sha256:c988a7c095b79a27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [WebSocket](../websocket.md)

# maximumMessageSize(_:)

<sub>Instance Method</sub>

Set the maximum allowed message size to be received by the WebSocket connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func maximumMessageSize(_ size: Int) -> WebSocket
```

## Parameters

- `size` — The maximum message size.

## Discussion

This does not limit the sending message size.

A maximum message size of 0 means there is no receive limit. The default maximum message size is 0.
