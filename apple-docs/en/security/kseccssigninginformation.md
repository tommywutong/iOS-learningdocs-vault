---
title: kSecCSSigningInformation
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccssigninginformation
source_url: 'https://developer.apple.com/documentation/security/kseccssigninginformation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccssigninginformation.json'
content_hash: 'sha256:fb2b2567ea232ff1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCSSigningInformation

<sub>Global Variable</sub>

Cryptographic signing information.

<sub>Mac Catalyst, macOS</sub>

```swift
var kSecCSSigningInformation: UInt32 { get }
```

## Discussion

The certificate chain and Cryptographic Message Syntax (CMS) data (if any). For ad-hoc signed code, there are no certificates and the CMS data is empty.
