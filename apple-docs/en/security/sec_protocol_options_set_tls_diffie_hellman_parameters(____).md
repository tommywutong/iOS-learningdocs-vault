---
title: 'sec_protocol_options_set_tls_diffie_hellman_parameters(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+（13.0 起废弃）, iPadOS 12.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.14+（10.15 起废弃）, tvOS 12.0+（13.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 5.0+（6.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sec_protocol_options_set_tls_diffie_hellman_parameters(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_options_set_tls_diffie_hellman_parameters(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_options_set_tls_diffie_hellman_parameters%28_%3A_%3A%29.json'
content_hash: 'sha256:0f5e111150e09c6c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_options_set_tls_diffie_hellman_parameters(_:_:)

<sub>Function</sub>

> [!warning] Deprecated
> DHE ciphersuites are no longer supported

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_options_set_tls_diffie_hellman_parameters(_ options: sec_protocol_options_t, _ params: dispatch_data_t)
```

## Parameters

- `options` — A `sec_protocol_options_t` instance.

- `params` — A dispatch_data_t containing legacy Diffie-Hellman parameters.

## Discussion

Set the supported Diffie-Hellman parameters.
