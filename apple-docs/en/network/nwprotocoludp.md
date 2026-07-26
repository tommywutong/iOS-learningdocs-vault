---
title: NWProtocolUDP
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocoludp
source_url: 'https://developer.apple.com/documentation/network/nwprotocoludp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocoludp.json'
content_hash: 'sha256:fa0f72fdd7f317e6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NWProtocolUDP

<sub>Class</sub>

A network protocol for connections that use the User Datagram Protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NWProtocolUDP
```

## Relationships

- **Inherits From**: [NWProtocol](nwprotocol.md)

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating UDP Connections

- [Options](nwprotocoludp/options.md) — A container of options for configuring how UDP is used on a connection.
- [definition](nwprotocoludp/definition.md) — The system definition of the User Datagram Protocol.

### Sending UDP Messages

- [Metadata](nwprotocoludp/metadata.md) — A container representing UDP when sending and receiving packets.

## See Also

### Network Protocols

- [Building a custom peer-to-peer protocol](building-a-custom-peer-to-peer-protocol.md) — Use networking frameworks to create a custom protocol for playing a game across iOS, iPadOS, watchOS, and tvOS devices.
- [Connecting iPadOS and visionOS apps over the local network](../visionos/connecting-ipados-and-visionos-apps-over-the-local-network.md) — Build an iPadOS companion app to control your visionOS app.
- [NWProtocolTCP](nwprotocoltcp.md) — A network protocol for connections that use the Transmission Control Protocol.
- [NWProtocolTLS](nwprotocoltls.md) — A network protocol for connections that use Transport Layer Security.
- [NWProtocolQUIC](nwprotocolquic.md) — A network protocol for connections that use the QUIC transport protocol.
- [NWProtocolIP](nwprotocolip.md) — A network protocol for configuring the Internet Protocol on connections.
- [NWProtocolWebSocket](nwprotocolwebsocket.md) — A network protocol for connections that use WebSocket.
- [NWProtocolFramer](nwprotocolframer.md) — A customizable network protocol for defining application message parsers.
