---
title: TLS
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/tls
source_url: 'https://developer.apple.com/documentation/network/tls'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tls.json'
content_hash: 'sha256:3a5ddf05bda6b2c2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# TLS

<sub>Structure</sub>

The system definition of the Transport Layer Security (TLS) protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TLS
```

## Overview

Supports sending and receiving encrypted byte streams.

## Relationships

- **Conforms To**: [NetworkProtocolOptions](networkprotocoloptions.md), [OneToOneProtocol](onetooneprotocol.md), [StreamProtocol](streamprotocol.md)

## Topics

### Initializers

- [init()](<tls/init().md>) — Create a TLS protocol to use in a protocol stack.
- [init(_:)](<tls/init(__).md>) — Create a TLS protocol to use in a protocol stack.

### Instance Methods

- [applicationProtocols(_:)](<tls/applicationprotocols(__).md>) — Set application protocols supported by clients of this protocol.
- [certificateValidator(_:)](<tls/certificatevalidator(__).md>) — Set a closure to provide custom verification of the peer’s credentials during the TLS handshake.
- [cipherSuiteGroups(_:)](<tls/ciphersuitegroups(__).md>) — Set TLS ciphersuite groups to the set of enabled ciphersuites.
- [cipherSuites(_:)](<tls/ciphersuites(__).md>) — Set TLS ciphersuites to the set of enabled ciphersuites.
- [earlyDataEnabled(_:)](<tls/earlydataenabled(__).md>) — Enable early data (0-RTT) for TLS.
- [localIdentity(_:)](<tls/localidentity(__).md>) — Set the local identity TLS uses during the handshake.
- [peerAuthentication(_:)](<tls/peerauthentication(__).md>) — Specify a preference for how to authenticate the peer.
- [ticketsEnabled(_:)](<tls/ticketsenabled(__).md>) — Enable TLS session ticket support.
- [version(min:max:)](<tls/version(min_max_).md>)

### Enumerations

- [PeerAuthentication](tls/peerauthentication.md) — PeerAuthentication specifies how to authenticate the peer end of the connection.
