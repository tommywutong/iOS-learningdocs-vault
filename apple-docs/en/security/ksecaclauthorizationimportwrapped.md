---
title: kSecACLAuthorizationImportWrapped
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecaclauthorizationimportwrapped
source_url: 'https://developer.apple.com/documentation/security/ksecaclauthorizationimportwrapped'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecaclauthorizationimportwrapped.json'
content_hash: 'sha256:1e32e175e3c3f886'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecACLAuthorizationImportWrapped

<sub>Global Variable</sub>

Import an encrypted key. This tag is checked on the key being imported; in addition, the `CSSM_ACL_AUTHORIZATION_DECRYPT` tag is checked for any key used in the unwrapping operation.

<sub>macOS</sub>

```swift
let kSecACLAuthorizationImportWrapped: CFString
```
