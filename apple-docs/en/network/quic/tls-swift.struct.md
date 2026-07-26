---
title: QUIC.TLS
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/quic/tls-swift.struct
source_url: 'https://developer.apple.com/documentation/network/quic/tls-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/quic/tls-swift.struct.json'
content_hash: 'sha256:ed83d07a19e0d95a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [QUIC](../quic.md)

# QUIC.TLS

<sub>Structure</sub>

The set of TLS options available when using QUIC.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TLS
```

## Overview

Used to configure the TLS handshake that runs within the QUIC handshake.

## Topics

### Instance Methods

- [certificateValidator(_:)](<tls-swift.struct/certificatevalidator(__).md>) — Set a block to provide custom verification of the peer’s credentials during the TLS handshake.
- [cipherSuites(_:)](<tls-swift.struct/ciphersuites(__).md>) — Set TLS cipher suites to the set of enabled ciphersuites.
- [ciphersuiteGroups(_:)](<tls-swift.struct/ciphersuitegroups(__).md>) — Set TLS cipher suite groups to the set of enabled ciphersuites.
- [localIdentity(_:)](<tls-swift.struct/localidentity(__).md>) — Set the local identity TLS uses during the QUIC handshake.
- [peerAuthentication(_:)](<tls-swift.struct/peerauthentication(__).md>) — Specify a preference for how to authenticate the peer.
