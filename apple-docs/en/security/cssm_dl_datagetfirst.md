---
title: CSSM_DL_DataGetFirst
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_dl_datagetfirst
source_url: 'https://developer.apple.com/documentation/security/cssm_dl_datagetfirst'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_dl_datagetfirst.json'
content_hash: 'sha256:d85cdfd024403284'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_DL_DataGetFirst

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_DL_DataGetFirst(CSSM_DL_DB_HANDLE DLDBHandle, const CSSM_QUERY *Query, CSSM_HANDLE_PTR ResultsHandle, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR Attributes, CSSM_DATA_PTR Data, CSSM_DB_UNIQUE_RECORD_PTR*UniqueId);
```
