---
title: useSignRevocation
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sectrustsettingskeyusage/usesignrevocation
source_url: 'https://developer.apple.com/documentation/security/sectrustsettingskeyusage/usesignrevocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustsettingskeyusage/usesignrevocation.json'
content_hash: 'sha256:37a01c4ed8a9d706'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecTrustSettingsKeyUsage](../sectrustsettingskeyusage.md)

# useSignRevocation

<sub>Type Property</sub>

The key can be used to sign an OCSP (online certificate status protocol) message or CRL (certificate verification list), or to verify a signature.

<sub>Mac Catalyst, macOS</sub>

```swift
static var useSignRevocation: SecTrustSettingsKeyUsage { get }
```

## Discussion

OCSP messages and CRLs are used to revoke certificates.
