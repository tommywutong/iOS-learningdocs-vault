---
title: CSSM_DL_DbCreate
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_dl_dbcreate
source_url: 'https://developer.apple.com/documentation/security/cssm_dl_dbcreate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_dl_dbcreate.json'
content_hash: 'sha256:109f5930459414bd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_DL_DbCreate

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_DL_DbCreate(CSSM_DL_HANDLE DLHandle, const char *DbName, const CSSM_NET_ADDRESS *DbLocation, const CSSM_DBINFO *DBInfo, CSSM_DB_ACCESS_TYPE AccessRequest, const CSSM_RESOURCE_CONTROL_CONTEXT *CredAndAclEntry, const void *OpenParameters, CSSM_DB_HANDLE *DbHandle);
```
