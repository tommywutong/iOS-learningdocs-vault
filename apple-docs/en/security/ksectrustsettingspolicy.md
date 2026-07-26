---
title: kSecTrustSettingsPolicy
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksectrustsettingspolicy
source_url: 'https://developer.apple.com/documentation/security/ksectrustsettingspolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectrustsettingspolicy.json'
content_hash: 'sha256:a6bff2309fa5fd82'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTrustSettingsPolicy

<sub>Global Variable</sub>

A policy object specifying the certificate verification policy.

<sub>Mac Catalyst, macOS</sub>

```swift
var kSecTrustSettingsPolicy: String { get }
```

## Discussion

The value is a [SecPolicy](secpolicy.md) object.
