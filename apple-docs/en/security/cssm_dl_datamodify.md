---
title: CSSM_DL_DataModify
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_dl_datamodify
source_url: 'https://developer.apple.com/documentation/security/cssm_dl_datamodify'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_dl_datamodify.json'
content_hash: 'sha256:3fbd0b3241c49a71'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_DL_DataModify

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_DL_DataModify(CSSM_DL_DB_HANDLE DLDBHandle, CSSM_DB_RECORDTYPE RecordType, CSSM_DB_UNIQUE_RECORD_PTR UniqueRecordIdentifier, const CSSM_DB_RECORD_ATTRIBUTE_DATA *AttributesToBeModified, const SecAsn1Item *DataToBeModified, CSSM_DB_MODIFY_MODE ModifyMode);
```
