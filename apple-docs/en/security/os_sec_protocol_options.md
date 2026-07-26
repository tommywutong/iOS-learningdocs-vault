---
title: OS_sec_protocol_options
framework: Security
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/os_sec_protocol_options
source_url: 'https://developer.apple.com/documentation/security/os_sec_protocol_options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/os_sec_protocol_options.json'
content_hash: 'sha256:0536b9feea9c6890'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# OS_sec_protocol_options

<sub>Protocol</sub>

A `sec_protocol_options` instance is a container of options for security protocol instances, such as TLS. Protocol options are used to configure security protocols in the network stack. For example, clients may set the maximum and minimum allowed TLS versions through protocol options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol OS_sec_protocol_options : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
