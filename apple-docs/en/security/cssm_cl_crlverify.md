---
title: CSSM_CL_CrlVerify
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_cl_crlverify
source_url: 'https://developer.apple.com/documentation/security/cssm_cl_crlverify'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_cl_crlverify.json'
content_hash: 'sha256:25fb45ff9a982fd3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_CL_CrlVerify

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_CL_CrlVerify(CSSM_CL_HANDLE CLHandle, CSSM_CC_HANDLE CCHandle, const SecAsn1Item *CrlToBeVerified, const SecAsn1Item *SignerCert, const CSSM_FIELD *VerifyScope, uint32 ScopeSize);
```
