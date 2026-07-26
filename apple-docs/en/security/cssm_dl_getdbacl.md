---
title: CSSM_DL_GetDbAcl
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_dl_getdbacl
source_url: 'https://developer.apple.com/documentation/security/cssm_dl_getdbacl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_dl_getdbacl.json'
content_hash: 'sha256:1e4073e2a218529d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_DL_GetDbAcl

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_DL_GetDbAcl(CSSM_DL_DB_HANDLE DLDBHandle, const CSSM_STRING *SelectionTag, uint32 *NumberOfAclInfos, CSSM_ACL_ENTRY_INFO_PTR*AclInfos);
```
