---
title: 'cipherSuiteGroups(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/network/dtls/ciphersuitegroups(_:)'
source_url: 'https://developer.apple.com/documentation/network/dtls/ciphersuitegroups(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/dtls/ciphersuitegroups%28_%3A%29.json'
content_hash: 'sha256:56ad05b8385dde0d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [DTLS](../dtls.md)

# cipherSuiteGroups(_:)

<sub>Instance Method</sub>

Set DTLS ciphersuite groups to the set of enabled ciphersuites.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cipherSuiteGroups(_ groups: [tls_ciphersuite_group_t]) -> DTLS
```

## Parameters

- `groups` — The cipher suite groups to set.
