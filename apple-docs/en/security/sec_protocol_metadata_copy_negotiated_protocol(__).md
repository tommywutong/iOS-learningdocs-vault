---
title: 'sec_protocol_metadata_copy_negotiated_protocol(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 18.5+, iPadOS 18.5+, Mac Catalyst 18.5+, macOS 15.5+, tvOS 18.5+, visionOS 2.5+, watchOS 11.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_protocol_metadata_copy_negotiated_protocol(_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_metadata_copy_negotiated_protocol(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_metadata_copy_negotiated_protocol%28_%3A%29.json'
content_hash: 'sha256:ed86653a20706d39'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_metadata_copy_negotiated_protocol(_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_metadata_copy_negotiated_protocol(_ metadata: sec_protocol_metadata_t) -> UnsafePointer<CChar>?
```

## Parameters

- `metadata` — A `sec_protocol_metadata_t` instance.

## Return Value

A NULL-terminated string carrying the negotiated protocol.

## Discussion

Copy the application protocol negotiated, e.g., via the TLS ALPN extension. The caller is expected to `free` the output string when no longer needed.
