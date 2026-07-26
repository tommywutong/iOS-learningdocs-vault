---
title: 'sec_protocol_options_set_local_identity(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_protocol_options_set_local_identity(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_options_set_local_identity(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_options_set_local_identity%28_%3A_%3A%29.json'
content_hash: 'sha256:214d2f121f6ac7c5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_options_set_local_identity(_:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_options_set_local_identity(_ options: sec_protocol_options_t, _ identity: sec_identity_t)
```

## Parameters

- `options` — A `sec_protocol_options_t` instance.

- `identity` — A `sec_identity_t` instance carrying the private key and certificate.

## Discussion

Set the local identity to be used for this protocol instance.
