---
title: sec_protocol_options_t
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sec_protocol_options_t
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_options_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_options_t.json'
content_hash: 'sha256:a822361a987ddd37'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_options_t

<sub>Type Alias</sub>

A `sec_protocol_options` instance is a container of options for security protocol instances, such as TLS. Protocol options are used to configure security protocols in the network stack. For example, clients may set the maximum and minimum allowed TLS versions through protocol options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias sec_protocol_options_t = any OS_sec_protocol_options
```
