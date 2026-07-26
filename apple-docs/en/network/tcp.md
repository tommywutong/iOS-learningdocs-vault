---
title: TCP
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/tcp
source_url: 'https://developer.apple.com/documentation/network/tcp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tcp.json'
content_hash: 'sha256:57e2ecd0b023d912'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# TCP

<sub>Structure</sub>

The system definition of the Transmission Control Protocol (TCP).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TCP
```

## Overview

Supports sending and receiving byte streams.

## Relationships

- **Conforms To**: [NetworkProtocolOptions](networkprotocoloptions.md), [OneToOneProtocol](onetooneprotocol.md), [StreamProtocol](streamprotocol.md)

## Topics

### Initializers

- [init()](<tcp/init().md>) — Create an instance of TCP.
- [init(_:)](<tcp/init(__).md>) — Create an instance of TCP.

### Instance Methods

- [ackStretchingDisabled(_:)](<tcp/ackstretchingdisabled(__).md>) — Disable ACK stretching.
- [connectionTimeout(_:)](<tcp/connectiontimeout(__).md>) — Set the timeout for TCP connection establishment.
- [ecnDisabled(_:)](<tcp/ecndisabled(__).md>) — Disable ECN negotiation.
- [fastOpenAllowed(_:)](<tcp/fastopenallowed(__).md>) — Configure TCP to enable TCP Fast Open (TFO).
- [keepalive(idleTimeInSeconds:count:intervalInSeconds:)](<tcp/keepalive(idletimeinseconds_count_intervalinseconds_).md>) — Enable TCP keepalives.
- [maximumSegmentSize(_:)](<tcp/maximumsegmentsize(__).md>) — Set maximum segment size.
- [noDelay(_:)](<tcp/nodelay(__).md>) — Disable Nagle’s algorithm.
- [noOptions(_:)](<tcp/nooptions(__).md>) — Enable no-options mode.
- [noPush(_:)](<tcp/nopush(__).md>) — Enable no-push mode.
- [persistTimeout(_:)](<tcp/persisttimeout(__).md>) — Set the TCP persist timeout.
- [retransmitConnectionDropTime(_:)](<tcp/retransmitconnectiondroptime(__).md>) — Set the TCP retransmission attempt timeout.
- [retransmitFinDrop(_:)](<tcp/retransmitfindrop(__).md>) — Configure TCP to drop the connection after a FIN does not receive an ACK.
