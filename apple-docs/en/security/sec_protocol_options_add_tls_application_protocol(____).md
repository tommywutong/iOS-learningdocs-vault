---
title: 'sec_protocol_options_add_tls_application_protocol(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_protocol_options_add_tls_application_protocol(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_options_add_tls_application_protocol(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_options_add_tls_application_protocol%28_%3A_%3A%29.json'
content_hash: 'sha256:efbc7af35db9b468'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_options_add_tls_application_protocol(_:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_options_add_tls_application_protocol(_ options: sec_protocol_options_t, _ application_protocol: UnsafePointer<CChar>)
```

## Parameters

- `options` — A `sec_protocol_options_t` instance.

- `application_protocol` — A NULL-terminated string defining the application protocol.

## Discussion

Add an application protocol supported by clients of this protocol instance.
