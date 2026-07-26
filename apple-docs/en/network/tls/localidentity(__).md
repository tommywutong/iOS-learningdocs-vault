---
title: 'localIdentity(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/tls/localidentity(_:)'
source_url: 'https://developer.apple.com/documentation/network/tls/localidentity(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tls/localidentity%28_%3A%29.json'
content_hash: 'sha256:a58887981894f974'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [TLS](../tls.md)

# localIdentity(_:)

<sub>Instance Method</sub>

Set the local identity TLS uses during the handshake.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func localIdentity(_ identity: sec_identity_t) -> TLS
```

## Parameters

- `identity` — The local identity to be used during the TLS handshake.
