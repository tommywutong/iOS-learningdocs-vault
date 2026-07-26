---
title: 'sec_protocol_metadata_peers_are_equal(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_protocol_metadata_peers_are_equal(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_metadata_peers_are_equal(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_metadata_peers_are_equal%28_%3A_%3A%29.json'
content_hash: 'sha256:df4264b93b0a7e11'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_metadata_peers_are_equal(_:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_metadata_peers_are_equal(_ metadataA: sec_protocol_metadata_t, _ metadataB: sec_protocol_metadata_t) -> Bool
```

## Parameters

- `metadataA` — A `sec_protocol_metadata_t` instance.

- `metadataB` — A `sec_protocol_metadata_t` instance.

## Return Value

Returns true if both metadata values refer to the same peer, and false otherwise.

## Discussion

Compare peer information for two `sec_protocol_metadata` instances. This comparison does not include protocol configuration options, e.g., ciphersuites.
