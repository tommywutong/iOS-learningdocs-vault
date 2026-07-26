---
title: 'init(_:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/websocket/init(_:)-7xsae'
source_url: 'https://developer.apple.com/documentation/network/websocket/init(_:)-7xsae'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/websocket/init%28_%3A%29-7xsae.json'
content_hash: 'sha256:64c46177edffd29d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [WebSocket](../websocket.md)

# init(_:)

<sub>Initializer</sub>

Create an instance of the WebSocket protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<BelowProtocol>(@ProtocolStackBuilder<BelowProtocol> _ builder: () -> BelowProtocol) where BelowProtocol : StreamProtocol
```

## Parameters

- `builder` — The protocol stack below WebSocket.
