---
title: QUICStream
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/quicstream
source_url: 'https://developer.apple.com/documentation/network/quicstream'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/quicstream.json'
content_hash: 'sha256:a777f668bf8e36c2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# QUICStream

<sub>Structure</sub>

A QUIC stream that runs over a QUIC connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct QUICStream
```

## Overview

Connections using QUICStream have a similar stream interface to TLS and TCP.

> [!note] Note
> This type is not intended to be inserted into the protocol stack manually; it is vended by connections that use QUIC.

## Relationships

- **Conforms To**: [NetworkProtocolOptions](networkprotocoloptions.md), [OneToOneProtocol](onetooneprotocol.md), [StreamProtocol](streamprotocol.md)

## Topics

### Enumerations

- [Directionality](quicstream/directionality.md)
- [Initiator](quicstream/initiator.md)
