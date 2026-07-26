---
title: NWProtocolWebSocket.Metadata
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolwebsocket/metadata
source_url: 'https://developer.apple.com/documentation/network/nwprotocolwebsocket/metadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolwebsocket/metadata.json'
content_hash: 'sha256:14314135ffead412'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWProtocolWebSocket](../nwprotocolwebsocket.md)

# NWProtocolWebSocket.Metadata

<sub>Class</sub>

A WebSocket message you configure when sending and receiving packets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Metadata
```

## Relationships

- **Inherits From**: [NWProtocolMetadata](../nwprotocolmetadata.md)

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Sending Messages

- [init(opcode:)](<metadata/init(opcode_).md>) — Initializes a WebSocket message with a specific type code.
- [Opcode](opcode.md) — Types of messages that you send and receive on a WebSocket connection.
- [setPongHandler(_:handler:)](<metadata/setponghandler(__handler_).md>) — Sets a handler on a Ping message to be invoked when the corresponding Pong message is received.
- [closeCode](metadata/closecode.md) — The close code on a WebSocket message.
- [CloseCode](closecode.md) — Types of codes used upon closing a WebSocket connection.

### Receiving Messages

- [opcode](metadata/opcode.md) — The type code of a WebSocket message.
- [closeCode](metadata/closecode.md) — The close code on a WebSocket message.
- [CloseCode](closecode.md) — Types of codes used upon closing a WebSocket connection.

### Inspecting Handshake Results

- [selectedSubprotocol](metadata/selectedsubprotocol.md) — The subprotocol selected by the server during the WebSocket handshake.
- [additionalServerHeaders](metadata/additionalserverheaders.md) — Additional HTTP headers sent by the server during the WebSocket handshake.
