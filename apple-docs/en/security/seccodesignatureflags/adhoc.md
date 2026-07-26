---
title: adhoc
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seccodesignatureflags/adhoc
source_url: 'https://developer.apple.com/documentation/security/seccodesignatureflags/adhoc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccodesignatureflags/adhoc.json'
content_hash: 'sha256:a304d2acd082cdab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecCodeSignatureFlags](../seccodesignatureflags.md)

# adhoc

<sub>Type Property</sub>

Must be used without a signing identity.

<sub>Mac Catalyst, macOS</sub>

```swift
static var adhoc: SecCodeSignatureFlags { get }
```

## Discussion

The code has been sealed without a signing identity. No identity may be retrieved from it, and any code requirement placing restrictions on the signing identity will fail. This flag is set by Code Signing Services when you create an ad-hoc signature, and cannot be set explicitly. An ad-hoc signature is created by signing with the pseudo-identity “-” (a dash).
