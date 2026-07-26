---
title: CSSM_ChangeKeyAcl
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_changekeyacl
source_url: 'https://developer.apple.com/documentation/security/cssm_changekeyacl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_changekeyacl.json'
content_hash: 'sha256:3aac36fa15c40eb8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_ChangeKeyAcl

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_ChangeKeyAcl(CSSM_CSP_HANDLE CSPHandle, const CSSM_ACCESS_CREDENTIALS *AccessCred, const CSSM_ACL_EDIT *AclEdit, const CSSM_KEY *Key);
```
