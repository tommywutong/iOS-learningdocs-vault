---
title: OneToOneProtocol
framework: Network
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/onetooneprotocol
source_url: 'https://developer.apple.com/documentation/network/onetooneprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/onetooneprotocol.json'
content_hash: 'sha256:947786f5db2e21be'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# OneToOneProtocol

<sub>Protocol</sub>

Types that conform to OneToOneProtocol are allowed to be the top protocol in a network protocol stack for non-multiplexed connections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol OneToOneProtocol : NetworkProtocolOptions
```

## Relationships

- **Inherits From**: [NetworkProtocolOptions](networkprotocoloptions.md)

- **Inherited By**: [DatagramProtocol](datagramprotocol.md), [MessageProtocol](messageprotocol.md), [StreamProtocol](streamprotocol.md)

- **Conforming Types**: [Coder](coder.md), [DTLS](dtls.md), [Framer](framer.md), [QUICDatagram](quicdatagram.md), [QUICStream](quicstream.md), [TCP](tcp.md), [TLS](tls.md), [TLV](tlv.md), [UDP](udp.md), [WebSocket](websocket.md)
