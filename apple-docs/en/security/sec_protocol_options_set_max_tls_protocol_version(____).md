---
title: 'sec_protocol_options_set_max_tls_protocol_version(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_protocol_options_set_max_tls_protocol_version(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_options_set_max_tls_protocol_version(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_options_set_max_tls_protocol_version%28_%3A_%3A%29.json'
content_hash: 'sha256:59e74dd8586fd1c8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_options_set_max_tls_protocol_version(_:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_options_set_max_tls_protocol_version(_ options: sec_protocol_options_t, _ version: tls_protocol_version_t)
```

## Parameters

- `options` — A `sec_protocol_options_t` instance.

- `version` — A tls_protocol_version_t enum value.

## Discussion

Set the maximum support TLS version.
