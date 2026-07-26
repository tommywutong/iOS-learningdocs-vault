---
title: sec_protocol_metadata_t
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sec_protocol_metadata_t
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_metadata_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_metadata_t.json'
content_hash: 'sha256:291c40eb64ba8e6f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_metadata_t

<sub>Type Alias</sub>

A `sec_protocol_metadata` instance conatins read-only properties of a connected and configured security protocol. Clients use this object to read information about a protocol instance. Properties include, for example, the negotiated TLS version, ciphersuite, and peer certificates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias sec_protocol_metadata_t = any OS_sec_protocol_metadata
```
