---
title: CSSM_CL_CertGetFirstCachedFieldValue
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_cl_certgetfirstcachedfieldvalue
source_url: 'https://developer.apple.com/documentation/security/cssm_cl_certgetfirstcachedfieldvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_cl_certgetfirstcachedfieldvalue.json'
content_hash: 'sha256:7c787dceeee4b04c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_CL_CertGetFirstCachedFieldValue

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_CL_CertGetFirstCachedFieldValue(CSSM_CL_HANDLE CLHandle, CSSM_HANDLE CertHandle, const SecAsn1Oid *CertField, CSSM_HANDLE_PTR ResultsHandle, uint32 *NumberOfMatchedFields, CSSM_DATA_PTR*Value);
```
