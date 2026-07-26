---
title: 'sec_protocol_metadata_access_ocsp_response(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_protocol_metadata_access_ocsp_response(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_metadata_access_ocsp_response(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_metadata_access_ocsp_response%28_%3A_%3A%29.json'
content_hash: 'sha256:ef109fadaf6103e0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_metadata_access_ocsp_response(_:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_metadata_access_ocsp_response(_ metadata: sec_protocol_metadata_t, _ handler: @escaping (dispatch_data_t) -> Void) -> Bool
```

## Parameters

- `metadata` — A `sec_protocol_metadata_t` instance.

- `handler` — A block to invoke one or more times with OCSP data

## Return Value

Returns true if the OSCP response was accessible, false otherwise.

## Discussion

Get the OCSP response from the protocol instance peer.
