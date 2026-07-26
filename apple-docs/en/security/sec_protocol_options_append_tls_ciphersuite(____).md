---
title: 'sec_protocol_options_append_tls_ciphersuite(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_protocol_options_append_tls_ciphersuite(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_options_append_tls_ciphersuite(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_options_append_tls_ciphersuite%28_%3A_%3A%29.json'
content_hash: 'sha256:9f16e0884d458687'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_options_append_tls_ciphersuite(_:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_options_append_tls_ciphersuite(_ options: sec_protocol_options_t, _ ciphersuite: tls_ciphersuite_t)
```

## Parameters

- `options` — A `sec_protocol_options_t` instance.

- `ciphersuite` — A `tls_ciphersuite_t` value.

## Discussion

Append a TLS ciphersuite to the set of enabled ciphersuites.
