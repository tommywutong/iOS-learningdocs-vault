---
title: 'cipherSuites(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/quic/tls-swift.struct/ciphersuites(_:)'
source_url: 'https://developer.apple.com/documentation/network/quic/tls-swift.struct/ciphersuites(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/quic/tls-swift.struct/ciphersuites%28_%3A%29.json'
content_hash: 'sha256:2ae54f78fda8715b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [QUIC](../../quic.md) · [TLS](../tls-swift.struct.md)

# cipherSuites(_:)

<sub>Instance Method</sub>

Set TLS cipher suites to the set of enabled ciphersuites.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cipherSuites(_ suites: [tls_ciphersuite_t]) -> QUIC
```

## Parameters

- `suites` — The cipher suites to set.
