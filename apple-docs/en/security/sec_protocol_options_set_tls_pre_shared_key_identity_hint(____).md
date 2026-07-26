---
title: 'sec_protocol_options_set_tls_pre_shared_key_identity_hint(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_protocol_options_set_tls_pre_shared_key_identity_hint(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_options_set_tls_pre_shared_key_identity_hint(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_options_set_tls_pre_shared_key_identity_hint%28_%3A_%3A%29.json'
content_hash: 'sha256:2a397e74f2eb8d35'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_options_set_tls_pre_shared_key_identity_hint(_:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_options_set_tls_pre_shared_key_identity_hint(_ options: sec_protocol_options_t, _ psk_identity_hint: dispatch_data_t)
```

## Parameters

- `options` — A `sec_protocol_options_t` instance.

- `psk_identity_hint` — A dispatch_data_t containing a PSK identity hint.

## Discussion

Set the PSK identity hint to use by servers when negotiating a PSK ciphersuite. See https://tools.ietf.org/html/rfc4279 for more details.
