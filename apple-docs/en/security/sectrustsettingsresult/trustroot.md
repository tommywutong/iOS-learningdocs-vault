---
title: SecTrustSettingsResult.trustRoot
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sectrustsettingsresult/trustroot
source_url: 'https://developer.apple.com/documentation/security/sectrustsettingsresult/trustroot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustsettingsresult/trustroot.json'
content_hash: 'sha256:be774c5e5bf6b5c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecTrustSettingsResult](../sectrustsettingsresult.md)

# SecTrustSettingsResult.trustRoot

<sub>Case</sub>

This root certificate is explicitly trusted.

<sub>Mac Catalyst, macOS</sub>

```swift
case trustRoot
```

## Discussion

If the certificate is not a root (self-signed) certificate, the usage constraints dictionary is invalid.
