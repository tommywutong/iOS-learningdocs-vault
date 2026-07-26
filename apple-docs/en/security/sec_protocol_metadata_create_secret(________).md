---
title: 'sec_protocol_metadata_create_secret(_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_protocol_metadata_create_secret(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_metadata_create_secret(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_metadata_create_secret%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:5127d65427a24d12'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_metadata_create_secret(_:_:_:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_metadata_create_secret(_ metadata: sec_protocol_metadata_t, _ label_len: Int, _ label: UnsafePointer<CChar>, _ exporter_length: Int) -> dispatch_data_t?
```

## Parameters

- `metadata` — A `sec_protocol_metadata_t` instance.

- `label_len` — Length of the KDF label string.

- `label` — KDF label string.

- `exporter_length` — Length of the secret to be exported.

## Return Value

Returns a dispatch_data_t object carrying the exported secret.

## Discussion

Export a secret, e.g., a cryptographic key, derived from the protocol metadata using a label string.
