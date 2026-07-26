---
title: UDP
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/udp
source_url: 'https://developer.apple.com/documentation/network/udp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/udp.json'
content_hash: 'sha256:72579608a8f527c8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# UDP

<sub>Structure</sub>

The system definition of the User Datagram Protocol (UDP).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct UDP
```

## Overview

UDP supports sending and receiving datagrams.

## Relationships

- **Conforms To**: [DatagramProtocol](datagramprotocol.md), [MessageProtocol](messageprotocol.md), [NetworkProtocolOptions](networkprotocoloptions.md), [OneToOneProtocol](onetooneprotocol.md)

## Topics

### Initializers

- [init()](<udp/init().md>)
- [init(_:)](<udp/init(__).md>)

### Instance Methods

- [noChecksumPreferred(_:)](<udp/nochecksumpreferred(__).md>) — Skip computing checksums when sending UDP packets.
