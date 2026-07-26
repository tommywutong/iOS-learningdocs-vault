---
title: CSSM_TP_CrlSign
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_tp_crlsign
source_url: 'https://developer.apple.com/documentation/security/cssm_tp_crlsign'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_tp_crlsign.json'
content_hash: 'sha256:f12d00c2ec26088b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_TP_CrlSign

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_TP_CrlSign(CSSM_TP_HANDLE TPHandle, CSSM_CL_HANDLE CLHandle, CSSM_CC_HANDLE CCHandle, const CSSM_ENCODED_CRL *CrlToBeSigned, const CSSM_CERTGROUP *SignerCertGroup, const CSSM_TP_VERIFY_CONTEXT *SignerVerifyContext, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR SignerVerifyResult, CSSM_DATA_PTR SignedCrl);
```
