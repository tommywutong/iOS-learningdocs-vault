---
title: sec_protocol_options_get_default_max_dtls_protocol_version()
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sec_protocol_options_get_default_max_dtls_protocol_version()
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_options_get_default_max_dtls_protocol_version()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_options_get_default_max_dtls_protocol_version%28%29.json'
content_hash: 'sha256:c6b0226d59012f15'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_options_get_default_max_dtls_protocol_version()

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_options_get_default_max_dtls_protocol_version() -> tls_protocol_version_t
```

## Return Value

The default maximum DTLS version.

## Discussion

Get the system default maximum DTLS protocol version.
