---
title: NWProtocolWebSocket
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolwebsocket
source_url: 'https://developer.apple.com/documentation/network/nwprotocolwebsocket'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolwebsocket.json'
content_hash: 'sha256:4a1572876ac9ac40'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NWProtocolWebSocket

<sub>Class</sub>

A network protocol for connections that use WebSocket.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NWProtocolWebSocket
```

## Relationships

- **Inherits From**: [NWProtocol](nwprotocol.md)

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating WebSocket Connections

- [Options](nwprotocolwebsocket/options.md) — A container of options for configuring how WebSocket is used on a connection.
- [definition](nwprotocolwebsocket/definition.md) — The system definition of the WebSocket protocol.

### Handling WebSocket Messages

- [Metadata](nwprotocolwebsocket/metadata.md) — A WebSocket message you configure when sending and receiving packets.

### Structures

- [Response](nwprotocolwebsocket/response.md) — A WebSocket handshake reponse sent from a server to a client.

### Enumerations

- [CloseCode](nwprotocolwebsocket/closecode.md) — Types of codes used upon closing a WebSocket connection.
- [Opcode](nwprotocolwebsocket/opcode.md) — Types of messages that you send and receive on a WebSocket connection.
- [Version](nwprotocolwebsocket/version.md) — Supported versions of the WebSocket protocol.

## See Also

### Network Protocols

- [Building a custom peer-to-peer protocol](building-a-custom-peer-to-peer-protocol.md) — Use networking frameworks to create a custom protocol for playing a game across iOS, iPadOS, watchOS, and tvOS devices.
- [Connecting iPadOS and visionOS apps over the local network](../visionos/connecting-ipados-and-visionos-apps-over-the-local-network.md) — Build an iPadOS companion app to control your visionOS app.
- [NWProtocolTCP](nwprotocoltcp.md) — A network protocol for connections that use the Transmission Control Protocol.
- [NWProtocolTLS](nwprotocoltls.md) — A network protocol for connections that use Transport Layer Security.
- [NWProtocolQUIC](nwprotocolquic.md) — A network protocol for connections that use the QUIC transport protocol.
- [NWProtocolUDP](nwprotocoludp.md) — A network protocol for connections that use the User Datagram Protocol.
- [NWProtocolIP](nwprotocolip.md) — A network protocol for configuring the Internet Protocol on connections.
- [NWProtocolFramer](nwprotocolframer.md) — A customizable network protocol for defining application message parsers.
