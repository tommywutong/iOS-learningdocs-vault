---
title: NWProtocolQUIC
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolquic
source_url: 'https://developer.apple.com/documentation/network/nwprotocolquic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolquic.json'
content_hash: 'sha256:3ef75c3224941265'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NWProtocolQUIC

<sub>Class</sub>

A network protocol for connections that use the QUIC transport protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NWProtocolQUIC
```

## Relationships

- **Inherits From**: [NWProtocol](nwprotocol.md)

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating QUIC Connections

- [Options](nwprotocolquic/options.md) — A container of options that configure the use of QUIC on a connection.
- [definition](nwprotocolquic/definition.md) — The system definition of the QUIC transport protocol.

### Inspecting QUIC State

- [Metadata](nwprotocolquic/metadata.md) — A handle you can use to inspect a connection’s QUIC state.

### Structures

- [ApplicationError](nwprotocolquic/applicationerror.md) — A QUIC application error code.

## See Also

### Network Protocols

- [Building a custom peer-to-peer protocol](building-a-custom-peer-to-peer-protocol.md) — Use networking frameworks to create a custom protocol for playing a game across iOS, iPadOS, watchOS, and tvOS devices.
- [Connecting iPadOS and visionOS apps over the local network](../visionos/connecting-ipados-and-visionos-apps-over-the-local-network.md) — Build an iPadOS companion app to control your visionOS app.
- [NWProtocolTCP](nwprotocoltcp.md) — A network protocol for connections that use the Transmission Control Protocol.
- [NWProtocolTLS](nwprotocoltls.md) — A network protocol for connections that use Transport Layer Security.
- [NWProtocolUDP](nwprotocoludp.md) — A network protocol for connections that use the User Datagram Protocol.
- [NWProtocolIP](nwprotocolip.md) — A network protocol for configuring the Internet Protocol on connections.
- [NWProtocolWebSocket](nwprotocolwebsocket.md) — A network protocol for connections that use WebSocket.
- [NWProtocolFramer](nwprotocolframer.md) — A customizable network protocol for defining application message parsers.
