---
title: CSSM_CSP_GetLoginAcl
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_csp_getloginacl
source_url: 'https://developer.apple.com/documentation/security/cssm_csp_getloginacl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_csp_getloginacl.json'
content_hash: 'sha256:446f79ed2e3941d1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_CSP_GetLoginAcl

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_CSP_GetLoginAcl(CSSM_CSP_HANDLE CSPHandle, const CSSM_STRING *SelectionTag, uint32 *NumberOfAclInfos, CSSM_ACL_ENTRY_INFO_PTR*AclInfos);
```
