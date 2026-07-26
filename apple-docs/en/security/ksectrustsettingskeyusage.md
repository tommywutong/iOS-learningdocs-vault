---
title: kSecTrustSettingsKeyUsage
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksectrustsettingskeyusage
source_url: 'https://developer.apple.com/documentation/security/ksectrustsettingskeyusage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectrustsettingskeyusage.json'
content_hash: 'sha256:266787f39d6a737e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTrustSettingsKeyUsage

<sub>Global Variable</sub>

A number specifying the operations for which the encryption key in this certificate can be used.

<sub>Mac Catalyst, macOS</sub>

```swift
var kSecTrustSettingsKeyUsage: String { get }
```

## Discussion

The value is a [CFNumber](../corefoundation/cfnumber.md) object containing an `SInt32` value.
