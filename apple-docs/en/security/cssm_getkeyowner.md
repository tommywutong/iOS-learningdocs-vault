---
title: CSSM_GetKeyOwner
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_getkeyowner
source_url: 'https://developer.apple.com/documentation/security/cssm_getkeyowner'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_getkeyowner.json'
content_hash: 'sha256:c5f51ecccb6db5aa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_GetKeyOwner

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_GetKeyOwner(CSSM_CSP_HANDLE CSPHandle, const CSSM_KEY *Key, CSSM_ACL_OWNER_PROTOTYPE_PTR Owner);
```
