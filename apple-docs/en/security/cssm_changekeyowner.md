---
title: CSSM_ChangeKeyOwner
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_changekeyowner
source_url: 'https://developer.apple.com/documentation/security/cssm_changekeyowner'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_changekeyowner.json'
content_hash: 'sha256:e0e13401127daa41'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_ChangeKeyOwner

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_ChangeKeyOwner(CSSM_CSP_HANDLE CSPHandle, const CSSM_ACCESS_CREDENTIALS *AccessCred, const CSSM_KEY *Key, const CSSM_ACL_OWNER_PROTOTYPE *NewOwner);
```
