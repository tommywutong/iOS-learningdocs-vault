---
title: 'skipHandshake(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/websocket/skiphandshake(_:)'
source_url: 'https://developer.apple.com/documentation/network/websocket/skiphandshake(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/websocket/skiphandshake%28_%3A%29.json'
content_hash: 'sha256:a88e1ee4583fac56'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [WebSocket](../websocket.md)

# skipHandshake(_:)

<sub>Instance Method</sub>

Configure the WebSocket protocol to skip the opening handshake and begin framing data as soon as the underlying connection is established.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func skipHandshake(_ skip: Bool) -> WebSocket
```

## Parameters

- `skip` — True to skip the handshake. Defaults to false.

## Discussion

> [!note] Note
> This option should not be set when communicating with a generic WebSocket server or client. This option allows a custom handshake (or no handshake) to be implemented below the WebSocket layer when both client and server are coordinated.
