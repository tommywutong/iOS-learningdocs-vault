---
title: 'autoReplyPing(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/websocket/autoreplyping(_:)'
source_url: 'https://developer.apple.com/documentation/network/websocket/autoreplyping(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/websocket/autoreplyping%28_%3A%29.json'
content_hash: 'sha256:5b0576c18296d30f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [WebSocket](../websocket.md)

# autoReplyPing(_:)

<sub>Instance Method</sub>

Configure the WebSocket protocol to automatically reply to pings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func autoReplyPing(_ reply: Bool) -> WebSocket
```

## Parameters

- `reply` — If true, ping messages will automatically be consumed by the connection instead of being delivered to the . Defaults to false.
