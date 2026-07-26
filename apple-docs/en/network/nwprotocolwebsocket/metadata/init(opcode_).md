---
title: 'init(opcode:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwprotocolwebsocket/metadata/init(opcode:)'
source_url: 'https://developer.apple.com/documentation/network/nwprotocolwebsocket/metadata/init(opcode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolwebsocket/metadata/init%28opcode%3A%29.json'
content_hash: 'sha256:7762b6000ab8f389'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolWebSocket](../../nwprotocolwebsocket.md) · [Metadata](../metadata.md)

# init(opcode:)

<sub>Initializer</sub>

Initializes a WebSocket message with a specific type code.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(opcode: NWProtocolWebSocket.Opcode)
```

## See Also

### Sending Messages

- [Opcode](../opcode.md) — Types of messages that you send and receive on a WebSocket connection.
- [setPongHandler(_:handler:)](<setponghandler(__handler_).md>) — Sets a handler on a Ping message to be invoked when the corresponding Pong message is received.
- [closeCode](closecode.md) — The close code on a WebSocket message.
- [CloseCode](../closecode.md) — Types of codes used upon closing a WebSocket connection.
