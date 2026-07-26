---
title: DTLS.PeerAuthentication.optional
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/network/dtls/peerauthentication/optional
source_url: 'https://developer.apple.com/documentation/network/dtls/peerauthentication/optional'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/dtls/peerauthentication/optional.json'
content_hash: 'sha256:beae3c5f60c10d51'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [DTLS](../../dtls.md) · [PeerAuthentication](../peerauthentication.md)

# DTLS.PeerAuthentication.optional

<sub>Case</sub>

Requests the peer certificate, but if none is provided, proceed with the connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case optional
```

## Discussion

This is for servers. Clients will ignore this option.
