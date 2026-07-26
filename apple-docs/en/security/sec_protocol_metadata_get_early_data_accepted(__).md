---
title: 'sec_protocol_metadata_get_early_data_accepted(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_protocol_metadata_get_early_data_accepted(_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_metadata_get_early_data_accepted(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_metadata_get_early_data_accepted%28_%3A%29.json'
content_hash: 'sha256:35a0d17d6bf4ba80'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_metadata_get_early_data_accepted(_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_metadata_get_early_data_accepted(_ metadata: sec_protocol_metadata_t) -> Bool
```

## Parameters

- `metadata` — A `sec_protocol_metadata_t` instance.

## Return Value

A bool indicating if early data was accepted.

## Discussion

Determine if early data was accepted by the peer.
