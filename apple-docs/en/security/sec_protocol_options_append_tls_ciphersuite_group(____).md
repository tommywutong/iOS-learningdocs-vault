---
title: 'sec_protocol_options_append_tls_ciphersuite_group(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_protocol_options_append_tls_ciphersuite_group(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_options_append_tls_ciphersuite_group(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_options_append_tls_ciphersuite_group%28_%3A_%3A%29.json'
content_hash: 'sha256:9c59296ef13665c2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_options_append_tls_ciphersuite_group(_:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_options_append_tls_ciphersuite_group(_ options: sec_protocol_options_t, _ group: tls_ciphersuite_group_t)
```

## Parameters

- `options` — A `sec_protocol_options_t` instance.

- `group` — A tls_ciphersuite_group_t value.

## Discussion

Append a TLS ciphersuite group to the set of enabled ciphersuites.
