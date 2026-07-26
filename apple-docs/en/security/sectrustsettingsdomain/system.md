---
title: SecTrustSettingsDomain.system
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sectrustsettingsdomain/system
source_url: 'https://developer.apple.com/documentation/security/sectrustsettingsdomain/system'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustsettingsdomain/system.json'
content_hash: 'sha256:83fcbf70bd836b45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecTrustSettingsDomain](../sectrustsettingsdomain.md)

# SecTrustSettingsDomain.system

<sub>Case</sub>

System trust settings.

<sub>Mac Catalyst, macOS</sub>

```swift
case system
```

## Discussion

These trust settings are immutable and comprise the set of trusted root certificates supplied in macOS. These settings are read-only, even by root.
