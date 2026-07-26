---
title: CSSM_GetKeyAcl
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_getkeyacl
source_url: 'https://developer.apple.com/documentation/security/cssm_getkeyacl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_getkeyacl.json'
content_hash: 'sha256:126919ce259847d1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_GetKeyAcl

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_GetKeyAcl(CSSM_CSP_HANDLE CSPHandle, const CSSM_KEY *Key, const CSSM_STRING *SelectionTag, uint32 *NumberOfAclInfos, CSSM_ACL_ENTRY_INFO_PTR*AclInfos);
```
