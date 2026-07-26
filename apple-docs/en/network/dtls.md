---
title: DTLS
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/network/dtls
source_url: 'https://developer.apple.com/documentation/network/dtls'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/dtls.json'
content_hash: 'sha256:3571b84ef9316bbb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# DTLS

<sub>Structure</sub>

The system definition of the Datagram Transport Layer Security (DTLS) protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DTLS
```

## Overview

Supports sending and receiving encrypted byte datagrams.

## Relationships

- **Conforms To**: [DatagramProtocol](datagramprotocol.md), [MessageProtocol](messageprotocol.md), [NetworkProtocolOptions](networkprotocoloptions.md), [OneToOneProtocol](onetooneprotocol.md)

## Topics

### Initializers

- [init()](<dtls/init().md>) — Create a DTLS protocol to use in a protocol stack. _(beta)_
- [init(_:)](<dtls/init(__).md>) — Create a DTLS protocol to use in a protocol stack. _(beta)_

### Instance Methods

- [applicationProtocols(_:)](<dtls/applicationprotocols(__).md>) — Set application protocols supported by clients of this protocol. _(beta)_
- [certificateValidator(_:)](<dtls/certificatevalidator(__).md>) — Set a closure to provide custom verification of the peer’s credentials during the DTLS handshake. _(beta)_
- [cipherSuiteGroups(_:)](<dtls/ciphersuitegroups(__).md>) — Set DTLS ciphersuite groups to the set of enabled ciphersuites. _(beta)_
- [cipherSuites(_:)](<dtls/ciphersuites(__).md>) — Set DTLS ciphersuites to the set of enabled ciphersuites. _(beta)_
- [earlyDataEnabled(_:)](<dtls/earlydataenabled(__).md>) — Enable early data (0-RTT) for DTLS. _(beta)_
- [localIdentity(_:)](<dtls/localidentity(__).md>) — Set the local identity DTLS uses during the handshake. _(beta)_
- [peerAuthentication(_:)](<dtls/peerauthentication(__).md>) — Specify a preference for how to authenticate the peer. _(beta)_
- [ticketsEnabled(_:)](<dtls/ticketsenabled(__).md>) — Enable DTLS session ticket support. _(beta)_
- [version(min:max:)](<dtls/version(min_max_).md>) _(beta)_

### Enumerations

- [PeerAuthentication](dtls/peerauthentication.md) — PeerAuthentication specifies how to authenticate the peer end of the connection. _(beta)_
