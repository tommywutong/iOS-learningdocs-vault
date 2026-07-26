---
title: DatagramProtocol
framework: Network
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/datagramprotocol
source_url: 'https://developer.apple.com/documentation/network/datagramprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/datagramprotocol.json'
content_hash: 'sha256:83b8bc0447b69b82'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# DatagramProtocol

<sub>Protocol</sub>

Types that conform to DatagramProtocol send and receive messages with minimal or no metadata, usually constrained to a fixed maximum size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol DatagramProtocol : MessageProtocol
```

## Relationships

- **Inherits From**: [MessageProtocol](messageprotocol.md), [NetworkProtocolOptions](networkprotocoloptions.md), [OneToOneProtocol](onetooneprotocol.md)

- **Conforming Types**: [DTLS](dtls.md), [QUICDatagram](quicdatagram.md), [UDP](udp.md)
