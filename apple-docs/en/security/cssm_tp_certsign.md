---
title: CSSM_TP_CertSign
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_tp_certsign
source_url: 'https://developer.apple.com/documentation/security/cssm_tp_certsign'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_tp_certsign.json'
content_hash: 'sha256:721f4916979c5c23'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_TP_CertSign

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_TP_CertSign(CSSM_TP_HANDLE TPHandle, CSSM_CL_HANDLE CLHandle, CSSM_CC_HANDLE CCHandle, const SecAsn1Item *CertTemplateToBeSigned, const CSSM_CERTGROUP *SignerCertGroup, const CSSM_TP_VERIFY_CONTEXT *SignerVerifyContext, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR SignerVerifyResult, CSSM_DATA_PTR SignedCert);
```
