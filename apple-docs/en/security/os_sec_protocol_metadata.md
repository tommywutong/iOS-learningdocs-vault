---
title: OS_sec_protocol_metadata
framework: Security
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/os_sec_protocol_metadata
source_url: 'https://developer.apple.com/documentation/security/os_sec_protocol_metadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/os_sec_protocol_metadata.json'
content_hash: 'sha256:356850453854263b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# OS_sec_protocol_metadata

<sub>Protocol</sub>

A `sec_protocol_metadata` instance conatins read-only properties of a connected and configured security protocol. Clients use this object to read information about a protocol instance. Properties include, for example, the negotiated TLS version, ciphersuite, and peer certificates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol OS_sec_protocol_metadata : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
