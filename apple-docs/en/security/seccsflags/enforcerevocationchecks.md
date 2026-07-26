---
title: enforceRevocationChecks
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seccsflags/enforcerevocationchecks
source_url: 'https://developer.apple.com/documentation/security/seccsflags/enforcerevocationchecks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccsflags/enforcerevocationchecks.json'
content_hash: 'sha256:5ec69a812117ba19'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecCSFlags](../seccsflags.md)

# enforceRevocationChecks

<sub>Type Property</sub>

<sub>Mac Catalyst, macOS</sub>

```swift
static var enforceRevocationChecks: SecCSFlags { get }
```

## Discussion

Forces checking of certificates against revocation lists or OCSP (online certificate status protocol) regardless of preference settings.
