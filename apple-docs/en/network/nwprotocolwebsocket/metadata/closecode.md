---
title: closeCode
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolwebsocket/metadata/closecode
source_url: 'https://developer.apple.com/documentation/network/nwprotocolwebsocket/metadata/closecode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolwebsocket/metadata/closecode.json'
content_hash: 'sha256:17ebdb65bdc5a830'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolWebSocket](../../nwprotocolwebsocket.md) · [Metadata](../metadata.md)

# closeCode

<sub>Instance Property</sub>

The close code on a WebSocket message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var closeCode: NWProtocolWebSocket.CloseCode { get set }
```

## See Also

### Sending Messages

- [init(opcode:)](<init(opcode_).md>) — Initializes a WebSocket message with a specific type code.
- [Opcode](../opcode.md) — Types of messages that you send and receive on a WebSocket connection.
- [setPongHandler(_:handler:)](<setponghandler(__handler_).md>) — Sets a handler on a Ping message to be invoked when the corresponding Pong message is received.
- [CloseCode](../closecode.md) — Types of codes used upon closing a WebSocket connection.
