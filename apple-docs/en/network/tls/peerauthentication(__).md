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
doc_path: '/documentation/network/tls/peerauthentication(_:)'
source_url: 'https://developer.apple.com/documentation/network/tls/peerauthentication(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tls/peerauthentication%28_%3A%29.json'
content_hash: 'sha256:ac5783126a06cb52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [TLS](../tls.md)

# peerAuthentication(_:)

<sub>Instance Method</sub>

Specify a preference for how to authenticate the peer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func peerAuthentication(_ preference: TLS.PeerAuthentication) -> TLS
```

## Parameters

- `preference` — The peer authentication preference.
