---
title: 'localIdentity(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/network/dtls/localidentity(_:)'
source_url: 'https://developer.apple.com/documentation/network/dtls/localidentity(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/dtls/localidentity%28_%3A%29.json'
content_hash: 'sha256:3f9b776ee0a7c3f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [DTLS](../dtls.md)

# localIdentity(_:)

<sub>Instance Method</sub>

Set the local identity DTLS uses during the handshake.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func localIdentity(_ identity: sec_identity_t) -> DTLS
```

## Parameters

- `identity` — The local identity to be used during the DTLS handshake.
