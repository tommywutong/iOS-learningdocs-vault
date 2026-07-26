---
title: host
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seccodesignatureflags/host
source_url: 'https://developer.apple.com/documentation/security/seccodesignatureflags/host'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccodesignatureflags/host.json'
content_hash: 'sha256:fc6ce06d551739db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecCodeSignatureFlags](../seccodesignatureflags.md)

# host

<sub>Type Property</sub>

May host guest code.

<sub>Mac Catalyst, macOS</sub>

```swift
static var host: SecCodeSignatureFlags { get }
```

## Discussion

Indicates that the code may act as a host that controls and supervises guest code. If this flag is not set in a code signature, the code is never considered eligible to be a host, and any attempt to act like one is ignored or rejected.
