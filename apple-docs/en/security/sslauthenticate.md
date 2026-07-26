---
title: SSLAuthenticate
framework: Security
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sslauthenticate
source_url: 'https://developer.apple.com/documentation/security/sslauthenticate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslauthenticate.json'
content_hash: 'sha256:971be1208322625b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLAuthenticate

<sub>Enumeration</sub>

The flags that represent the requirements for client-side authentication.

<sub>Mac Catalyst, macOS</sub>

```swift
enum SSLAuthenticate
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kNeverAuthenticate](sslauthenticate/neverauthenticate.md) — Indicates that client-side authentication is not required. (Default.)
- [kAlwaysAuthenticate](sslauthenticate/alwaysauthenticate.md) — Indicates that client-side authentication is required.
- [kTryAuthenticate](sslauthenticate/tryauthenticate.md) — Indicates that client-side authentication should be attempted. There is no error if the client doesn’t have a certificate.

### Initializers

- [init(rawValue:)](<sslauthenticate/init(rawvalue_).md>)
