---
title: CSSM_CL_CrlSign
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_cl_crlsign
source_url: 'https://developer.apple.com/documentation/security/cssm_cl_crlsign'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_cl_crlsign.json'
content_hash: 'sha256:52c1d43350dce7ee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_CL_CrlSign

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_CL_CrlSign(CSSM_CL_HANDLE CLHandle, CSSM_CC_HANDLE CCHandle, const SecAsn1Item *UnsignedCrl, const CSSM_FIELD *SignScope, uint32 ScopeSize, CSSM_DATA_PTR SignedCrl);
```
