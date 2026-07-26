---
title: forceExpiration
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seccodesignatureflags/forceexpiration
source_url: 'https://developer.apple.com/documentation/security/seccodesignatureflags/forceexpiration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccodesignatureflags/forceexpiration.json'
content_hash: 'sha256:51c0f91afa689ce9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecCodeSignatureFlags](../seccodesignatureflags.md)

# forceExpiration

<sub>Type Property</sub>

Always set the [kSecCSConsiderExpiration](../seccsflags/considerexpiration.md) flag when validating the code.

<sub>Mac Catalyst, macOS</sub>

```swift
static var forceExpiration: SecCodeSignatureFlags { get }
```

## Discussion

When passed to a function that performs code validation, the `kSecCSConsiderExpiration` flag requests that code signatures made by expired certificates be rejected. By default, expiration of participating certificates is not automatic grounds for rejection.
