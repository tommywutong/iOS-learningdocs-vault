---
title: MessageProtocol
framework: Network
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/messageprotocol
source_url: 'https://developer.apple.com/documentation/network/messageprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/messageprotocol.json'
content_hash: 'sha256:4c06d15ecf39b51c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# MessageProtocol

<sub>Protocol</sub>

Types that conform to MessageProtocol send and receive messages. The conforming type is responsible for specifying its message-specific metadata.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol MessageProtocol : OneToOneProtocol
```

## Relationships

- **Inherits From**: [NetworkProtocolOptions](networkprotocoloptions.md), [OneToOneProtocol](onetooneprotocol.md)

- **Inherited By**: [DatagramProtocol](datagramprotocol.md)

- **Conforming Types**: [Coder](coder.md), [DTLS](dtls.md), [Framer](framer.md), [QUICDatagram](quicdatagram.md), [TLV](tlv.md), [UDP](udp.md), [WebSocket](websocket.md)

## Topics

### Associated Types

- [ContentType](messageprotocol/contenttype.md)
- [LegacyMessage](messageprotocol/legacymessage.md)
