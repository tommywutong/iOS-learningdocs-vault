---
title: 'peerAuthentication(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/quic/tls-swift.struct/peerauthentication(_:)'
source_url: 'https://developer.apple.com/documentation/network/quic/tls-swift.struct/peerauthentication(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/quic/tls-swift.struct/peerauthentication%28_%3A%29.json'
content_hash: 'sha256:be351a70ac9457cd'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [QUIC](../../quic.md) · [TLS](../tls-swift.struct.md)

# peerAuthentication(_:)

<sub>Instance Method</sub>

Specify a preference for how to authenticate the peer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func peerAuthentication(_ preference: TLS.PeerAuthentication) -> QUIC
```

## Parameters

- `preference` — The peer authentication preference.
