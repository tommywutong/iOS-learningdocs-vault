---
title: CSSM_DL_DataInsert
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_dl_datainsert
source_url: 'https://developer.apple.com/documentation/security/cssm_dl_datainsert'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_dl_datainsert.json'
content_hash: 'sha256:3cef0eaed9aa3ffa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_DL_DataInsert

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_DL_DataInsert(CSSM_DL_DB_HANDLE DLDBHandle, CSSM_DB_RECORDTYPE RecordType, const CSSM_DB_RECORD_ATTRIBUTE_DATA *Attributes, const SecAsn1Item *Data, CSSM_DB_UNIQUE_RECORD_PTR*UniqueId);
```
