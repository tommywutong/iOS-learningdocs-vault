---
title: 'sec_protocol_options_add_tls_ciphersuite(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+（13.0 起废弃）, iPadOS 12.0+（13.0 起废弃）, Mac Catalyst 12.0+（13.0 起废弃）, macOS 10.14+（10.15 起废弃）, tvOS 12.0+（13.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 5.0+（6.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sec_protocol_options_add_tls_ciphersuite(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_options_add_tls_ciphersuite(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_options_add_tls_ciphersuite%28_%3A_%3A%29.json'
content_hash: 'sha256:ad17737412544037'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_options_add_tls_ciphersuite(_:_:)

<sub>Function</sub>

> [!warning] Deprecated
> Use sec_protocol_options_append_tls_ciphersuite

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_options_add_tls_ciphersuite(_ options: sec_protocol_options_t, _ ciphersuite: SSLCipherSuite)
```

## Parameters

- `options` — A `sec_protocol_options_t` instance.

- `ciphersuite` — A SSLCipherSuite value.

## Discussion

Add a TLS ciphersuite to the set of enabled ciphersuites.
