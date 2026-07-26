---
title: NWProtocolFramer
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolframer
source_url: 'https://developer.apple.com/documentation/network/nwprotocolframer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolframer.json'
content_hash: 'sha256:c9734cd1dbb63c8f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NWProtocolFramer

<sub>Class</sub>

A customizable network protocol for defining application message parsers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NWProtocolFramer
```

## Relationships

- **Inherits From**: [NWProtocol](nwprotocol.md)

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Implementing Framer Protocols

- [NWProtocolFramerImplementation](nwprotocolframerimplementation.md) — A protocol to which your classes can conform in order to implement a custom framing protocol.
- [Instance](nwprotocolframer/instance.md) — An object that represents a single instance of your custom protocol running in a connection.

### Using Framers with Connections

- [Definition](nwprotocolframer/definition.md) — A custom protocol definition you use to associate messages with protocol options.
- [Options](nwprotocolframer/options.md) — A container you use to add your custom protocol to a connection’s protocol stack.
- [Message](nwprotocolframer/message.md) — A message for a custom protocol, in which you can store arbitrary key-value pairs.

### Enumerations

- [StartResult](nwprotocolframer/startresult.md) — Results that you send to indicate the disposition of your protocol after receiving the call to start.

## See Also

### Network Protocols

- [Building a custom peer-to-peer protocol](building-a-custom-peer-to-peer-protocol.md) — Use networking frameworks to create a custom protocol for playing a game across iOS, iPadOS, watchOS, and tvOS devices.
- [Connecting iPadOS and visionOS apps over the local network](../visionos/connecting-ipados-and-visionos-apps-over-the-local-network.md) — Build an iPadOS companion app to control your visionOS app.
- [NWProtocolTCP](nwprotocoltcp.md) — A network protocol for connections that use the Transmission Control Protocol.
- [NWProtocolTLS](nwprotocoltls.md) — A network protocol for connections that use Transport Layer Security.
- [NWProtocolQUIC](nwprotocolquic.md) — A network protocol for connections that use the QUIC transport protocol.
- [NWProtocolUDP](nwprotocoludp.md) — A network protocol for connections that use the User Datagram Protocol.
- [NWProtocolIP](nwprotocolip.md) — A network protocol for configuring the Internet Protocol on connections.
- [NWProtocolWebSocket](nwprotocolwebsocket.md) — A network protocol for connections that use WebSocket.
