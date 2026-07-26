---
title: 'sec_protocol_options_set_tls_server_name(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_protocol_options_set_tls_server_name(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_options_set_tls_server_name(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_options_set_tls_server_name%28_%3A_%3A%29.json'
content_hash: 'sha256:162987173283d70a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_options_set_tls_server_name(_:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_options_set_tls_server_name(_ options: sec_protocol_options_t, _ server_name: UnsafePointer<CChar>)
```

## Parameters

- `options` — A `sec_protocol_options_t` instance.

- `server_name` — A NULL-terminated string carrying the server name.

## Discussion

Set the server name to be used when verifying the peer’s certificate. This will override the server name obtained from the endpoint.
