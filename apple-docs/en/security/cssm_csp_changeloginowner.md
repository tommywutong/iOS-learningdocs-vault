---
title: CSSM_CSP_ChangeLoginOwner
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_csp_changeloginowner
source_url: 'https://developer.apple.com/documentation/security/cssm_csp_changeloginowner'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_csp_changeloginowner.json'
content_hash: 'sha256:3bd0025e498929ef'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_CSP_ChangeLoginOwner

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_CSP_ChangeLoginOwner(CSSM_CSP_HANDLE CSPHandle, const CSSM_ACCESS_CREDENTIALS *AccessCred, const CSSM_ACL_OWNER_PROTOTYPE *NewOwner);
```
