---
title: 'sec_protocol_options_add_pre_shared_key(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_protocol_options_add_pre_shared_key(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_options_add_pre_shared_key(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_options_add_pre_shared_key%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:6cbeb2624c9e161c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_options_add_pre_shared_key(_:_:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_options_add_pre_shared_key(_ options: sec_protocol_options_t, _ psk: dispatch_data_t, _ psk_identity: dispatch_data_t)
```

## Parameters

- `options` — A `sec_protocol_options_t` instance.

- `psk` — A dispatch_data_t containing a PSK blob.

- `psk_identity` — A dispatch_data_t containing a PSK identity blob.

## Discussion

Add a pre-shared key (PSK) and its identity to the options.
