---
title: MultiplexProtocol
framework: Network
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/multiplexprotocol
source_url: 'https://developer.apple.com/documentation/network/multiplexprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/multiplexprotocol.json'
content_hash: 'sha256:29a66e1edfadfbf9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# MultiplexProtocol

<sub>Protocol</sub>

Types that conform to MultiplexProtocol are allowed to be the top protocol in a network protocol stack for multiplexing network connection objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol MultiplexProtocol : NetworkProtocolOptions
```

## Overview

Generally network protocols conforming to this type will not directly expose send or receive methods. Instead, they expose methods to open and listen for multiplexed Subconnections which can send and receive.

## Relationships

- **Inherits From**: [NetworkProtocolOptions](networkprotocoloptions.md)

- **Conforming Types**: [QUIC](quic.md)
