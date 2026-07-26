---
title: 'cipherSuites(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/network/dtls/ciphersuites(_:)'
source_url: 'https://developer.apple.com/documentation/network/dtls/ciphersuites(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/dtls/ciphersuites%28_%3A%29.json'
content_hash: 'sha256:12fc1458a306d420'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [DTLS](../dtls.md)

# cipherSuites(_:)

<sub>Instance Method</sub>

Set DTLS ciphersuites to the set of enabled ciphersuites.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cipherSuites(_ suites: [tls_ciphersuite_t]) -> DTLS
```

## Parameters

- `suites` — The cipher suites to set.
