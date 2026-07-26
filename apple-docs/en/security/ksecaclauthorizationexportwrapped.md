---
title: kSecACLAuthorizationExportWrapped
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecaclauthorizationexportwrapped
source_url: 'https://developer.apple.com/documentation/security/ksecaclauthorizationexportwrapped'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecaclauthorizationexportwrapped.json'
content_hash: 'sha256:480c306146a98df4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecACLAuthorizationExportWrapped

<sub>Global Variable</sub>

Export a wrapped (that is, encrypted) key. This tag is checked on the key being exported; in addition, the `CSSM_ACL_AUTHORIZATION_ENCRYPT` tag is checked for any key used in the wrapping operation.

<sub>macOS</sub>

```swift
let kSecACLAuthorizationExportWrapped: CFString
```
