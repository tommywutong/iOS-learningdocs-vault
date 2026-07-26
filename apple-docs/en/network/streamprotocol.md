---
title: StreamProtocol
framework: Network
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/streamprotocol
source_url: 'https://developer.apple.com/documentation/network/streamprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/streamprotocol.json'
content_hash: 'sha256:badc85a4a7bee96a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# StreamProtocol

<sub>Protocol</sub>

Types that conform to the StreamProtocol protocol expose methods for sending and receiving byte streams.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol StreamProtocol : OneToOneProtocol
```

## Relationships

- **Inherits From**: [NetworkProtocolOptions](networkprotocoloptions.md), [OneToOneProtocol](onetooneprotocol.md)

- **Conforming Types**: [QUICStream](quicstream.md), [TCP](tcp.md), [TLS](tls.md)
