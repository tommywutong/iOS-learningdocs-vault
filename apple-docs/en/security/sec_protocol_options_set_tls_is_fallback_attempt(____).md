---
title: 'sec_protocol_options_set_tls_is_fallback_attempt(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_protocol_options_set_tls_is_fallback_attempt(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_options_set_tls_is_fallback_attempt(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_options_set_tls_is_fallback_attempt%28_%3A_%3A%29.json'
content_hash: 'sha256:b1ff5d9077a15346'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_options_set_tls_is_fallback_attempt(_:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_options_set_tls_is_fallback_attempt(_ options: sec_protocol_options_t, _ is_fallback_attempt: Bool)
```

## Parameters

- `options` — A `sec_protocol_options_t` instance.

- `is_fallback_attempt` — Set a flag indicating that this is a TLS fallback attempt.

## Discussion

Signal if this is a TLS fallback attempt.

```
 A fallback attempt is one following a previously failed TLS connection
 due to version or parameter incompatibility, e.g., when speaking to a server
 that does not support a client-offered ciphersuite.

 Clients MUST NOT enable fallback for fresh connections.
```
