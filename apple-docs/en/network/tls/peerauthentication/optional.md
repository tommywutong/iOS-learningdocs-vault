---
title: TLS.PeerAuthentication.optional
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/tls/peerauthentication/optional
source_url: 'https://developer.apple.com/documentation/network/tls/peerauthentication/optional'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tls/peerauthentication/optional.json'
content_hash: 'sha256:19504703890baf56'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [TLS](../../tls.md) · [PeerAuthentication](../peerauthentication.md)

# TLS.PeerAuthentication.optional

<sub>Case</sub>

Requests the peer certificate, but if none is provided, proceed with the connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case optional
```

## Discussion

This is for servers. Clients will ignore this option.
