---
title: 'sec_protocol_metadata_copy_peer_public_key(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_protocol_metadata_copy_peer_public_key(_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_metadata_copy_peer_public_key(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_metadata_copy_peer_public_key%28_%3A%29.json'
content_hash: 'sha256:c4349f057b657d98'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_metadata_copy_peer_public_key(_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_metadata_copy_peer_public_key(_ metadata: sec_protocol_metadata_t) -> dispatch_data_t?
```

## Parameters

- `metadata` — A `sec_protocol_metadata_t` instance.

## Return Value

A `dispatch_data_t` containing the peer’s raw public key.

## Discussion

Get the protocol instance peer’s public key.
