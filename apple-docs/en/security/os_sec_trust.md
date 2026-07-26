---
title: OS_sec_trust
framework: Security
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/os_sec_trust
source_url: 'https://developer.apple.com/documentation/security/os_sec_trust'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/os_sec_trust.json'
content_hash: 'sha256:d3543b0b8dea64eb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# OS_sec_trust

<sub>Protocol</sub>

These are os_object compatible and ARC-able wrappers around existing CoreFoundation Security types, including: SecTrustRef, SecIdentityRef, and SecCertificateRef. They allow clients to use these types in os_object-type APIs and data structures. The underlying CoreFoundation types may be extracted and used by clients as needed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol OS_sec_trust : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
