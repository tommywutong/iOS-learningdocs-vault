---
title: CSSM_TP_ApplyCrlToDb
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_tp_applycrltodb
source_url: 'https://developer.apple.com/documentation/security/cssm_tp_applycrltodb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_tp_applycrltodb.json'
content_hash: 'sha256:a857a14c11911d6d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_TP_ApplyCrlToDb

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_TP_ApplyCrlToDb(CSSM_TP_HANDLE TPHandle, CSSM_CL_HANDLE CLHandle, CSSM_CSP_HANDLE CSPHandle, const CSSM_ENCODED_CRL *CrlToBeApplied, const CSSM_CERTGROUP *SignerCertGroup, const CSSM_TP_VERIFY_CONTEXT *ApplyCrlVerifyContext, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR ApplyCrlVerifyResult);
```
