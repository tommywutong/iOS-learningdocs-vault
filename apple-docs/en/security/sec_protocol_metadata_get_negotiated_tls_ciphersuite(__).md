---
title: 'sec_protocol_metadata_get_negotiated_tls_ciphersuite(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_protocol_metadata_get_negotiated_tls_ciphersuite(_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_metadata_get_negotiated_tls_ciphersuite(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_metadata_get_negotiated_tls_ciphersuite%28_%3A%29.json'
content_hash: 'sha256:fbe7c84c3794aab3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_metadata_get_negotiated_tls_ciphersuite(_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_metadata_get_negotiated_tls_ciphersuite(_ metadata: sec_protocol_metadata_t) -> tls_ciphersuite_t
```

## Parameters

- `metadata` — A `sec_protocol_metadata_t` instance.

## Return Value

A `tls_ciphersuite_t`.

## Discussion

Get the negotiated TLS ciphersuite.
