---
title: 'sec_protocol_metadata_get_negotiated_protocol(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+（18.5 起废弃）, iPadOS 12.0+（18.5 起废弃）, Mac Catalyst 13.1+（18.5 起废弃）, macOS 10.14+（15.5 起废弃）, tvOS 12.0+（18.5 起废弃）, visionOS 1.0+（2.5 起废弃）, watchOS 5.0+（11.5 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sec_protocol_metadata_get_negotiated_protocol(_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_metadata_get_negotiated_protocol(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_metadata_get_negotiated_protocol%28_%3A%29.json'
content_hash: 'sha256:ef285382672b5072'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_metadata_get_negotiated_protocol(_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_metadata_get_negotiated_protocol(_ metadata: sec_protocol_metadata_t) -> UnsafePointer<CChar>?
```

## Parameters

- `metadata` — A `sec_protocol_metadata_t` instance.

## Return Value

A NULL-terminated string carrying the negotiated protocol.

## Discussion

Get the application protocol negotiated, e.g., via the TLS ALPN extension.
