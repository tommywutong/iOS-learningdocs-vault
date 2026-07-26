---
title: kSecTrustSettingsApplication
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksectrustsettingsapplication
source_url: 'https://developer.apple.com/documentation/security/ksectrustsettingsapplication'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectrustsettingsapplication.json'
content_hash: 'sha256:18f0c38b90b6b287'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTrustSettingsApplication

<sub>Global Variable</sub>

A trusted application reference for the application checking the certificate’s trust settings.

<sub>Mac Catalyst, macOS</sub>

```swift
var kSecTrustSettingsApplication: String { get }
```

## Discussion

The value is a [SecTrustedApplication](sectrustedapplication.md) object.
