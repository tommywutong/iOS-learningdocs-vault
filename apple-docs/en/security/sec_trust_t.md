---
title: sec_trust_t
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sec_trust_t
source_url: 'https://developer.apple.com/documentation/security/sec_trust_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_trust_t.json'
content_hash: 'sha256:f7de25a2558dc5fe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_trust_t

<sub>Type Alias</sub>

These are os_object compatible and ARC-able wrappers around existing CoreFoundation Security types, including: SecTrustRef, SecIdentityRef, and SecCertificateRef. They allow clients to use these types in os_object-type APIs and data structures. The underlying CoreFoundation types may be extracted and used by clients as needed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias sec_trust_t = any OS_sec_trust
```
