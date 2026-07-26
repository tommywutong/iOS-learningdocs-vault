---
title: 'cipherSuiteGroups(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/tls/ciphersuitegroups(_:)'
source_url: 'https://developer.apple.com/documentation/network/tls/ciphersuitegroups(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tls/ciphersuitegroups%28_%3A%29.json'
content_hash: 'sha256:a7ccd5625424d8a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [TLS](../tls.md)

# cipherSuiteGroups(_:)

<sub>Instance Method</sub>

Set TLS ciphersuite groups to the set of enabled ciphersuites.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cipherSuiteGroups(_ groups: [tls_ciphersuite_group_t]) -> TLS
```

## Parameters

- `groups` — The cipher suite groups to set.
