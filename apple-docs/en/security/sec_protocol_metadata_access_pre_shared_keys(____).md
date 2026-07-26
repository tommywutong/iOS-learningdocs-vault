---
title: 'sec_protocol_metadata_access_pre_shared_keys(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_protocol_metadata_access_pre_shared_keys(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_metadata_access_pre_shared_keys(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_metadata_access_pre_shared_keys%28_%3A_%3A%29.json'
content_hash: 'sha256:f6720d8e58434621'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_metadata_access_pre_shared_keys(_:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_metadata_access_pre_shared_keys(_ metadata: sec_protocol_metadata_t, _ handler: @escaping (dispatch_data_t, dispatch_data_t) -> Void) -> Bool
```

## Parameters

- `metadata` — A `sec_protocol_metadata_t` instance.

- `handler` — A block to invoke one or more times with tuples of dispatch_data_t objects carrying PSKs and their corresponding identities.

## Return Value

Returns true if the PSKs were accessible, false otherwise.

## Discussion

Get the PSKs supported by the local instance.
