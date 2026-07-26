---
title: 'sec_protocol_metadata_get_negotiated_tls_protocol_version(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_protocol_metadata_get_negotiated_tls_protocol_version(_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_metadata_get_negotiated_tls_protocol_version(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_metadata_get_negotiated_tls_protocol_version%28_%3A%29.json'
content_hash: 'sha256:e5265f45465572ac'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_metadata_get_negotiated_tls_protocol_version(_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_metadata_get_negotiated_tls_protocol_version(_ metadata: sec_protocol_metadata_t) -> tls_protocol_version_t
```

## Parameters

- `metadata` — A `sec_protocol_metadata_t` instance.

## Return Value

A `tls_protocol_version_t` value.

## Discussion

Get the negotiated TLS version.
