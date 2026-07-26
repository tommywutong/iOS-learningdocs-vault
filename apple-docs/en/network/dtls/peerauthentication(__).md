---
title: 'peerAuthentication(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/network/dtls/peerauthentication(_:)'
source_url: 'https://developer.apple.com/documentation/network/dtls/peerauthentication(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/dtls/peerauthentication%28_%3A%29.json'
content_hash: 'sha256:c39616dc2bae3331'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [DTLS](../dtls.md)

# peerAuthentication(_:)

<sub>Instance Method</sub>

Specify a preference for how to authenticate the peer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func peerAuthentication(_ preference: DTLS.PeerAuthentication) -> DTLS
```

## Parameters

- `preference` — The peer authentication preference.
