---
title: CSSM_CL_CrlGetFirstCachedFieldValue
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_cl_crlgetfirstcachedfieldvalue
source_url: 'https://developer.apple.com/documentation/security/cssm_cl_crlgetfirstcachedfieldvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_cl_crlgetfirstcachedfieldvalue.json'
content_hash: 'sha256:cdd012c8d84cc80f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_CL_CrlGetFirstCachedFieldValue

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_CL_CrlGetFirstCachedFieldValue(CSSM_CL_HANDLE CLHandle, CSSM_HANDLE CrlHandle, const SecAsn1Item *CrlRecordIndex, const SecAsn1Oid *CrlField, CSSM_HANDLE_PTR ResultsHandle, uint32 *NumberOfMatchedFields, CSSM_DATA_PTR*Value);
```
