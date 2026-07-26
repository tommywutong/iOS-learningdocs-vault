---
title: 'sec_protocol_metadata_copy_server_name(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 18.5+, iPadOS 18.5+, Mac Catalyst 18.5+, macOS 15.5+, tvOS 18.5+, visionOS 2.5+, watchOS 11.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_protocol_metadata_copy_server_name(_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_metadata_copy_server_name(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_metadata_copy_server_name%28_%3A%29.json'
content_hash: 'sha256:60161baa40b74de8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_metadata_copy_server_name(_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_metadata_copy_server_name(_ metadata: sec_protocol_metadata_t) -> UnsafePointer<CChar>?
```

## Parameters

- `metadata` — A `sec_protocol_metadata_t` instance.

## Return Value

Returns A NULL-terminated string carrying the server name, or NULL if none was provided.

## Discussion

Obtain a copy of the server name offered by a client or server during connection establishmet. This is the value commonly carried in the TLS SNI extesion. The caller is expected to `free` the output string when it is no longer needed.
