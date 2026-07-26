---
title: CSSM_TP_CertRevoke
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_tp_certrevoke
source_url: 'https://developer.apple.com/documentation/security/cssm_tp_certrevoke'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_tp_certrevoke.json'
content_hash: 'sha256:32de35226d35a7fd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_TP_CertRevoke

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_TP_CertRevoke(CSSM_TP_HANDLE TPHandle, CSSM_CL_HANDLE CLHandle, CSSM_CSP_HANDLE CSPHandle, const SecAsn1Item *OldCrlTemplate, const CSSM_CERTGROUP *CertGroupToBeRevoked, const CSSM_CERTGROUP *RevokerCertGroup, const CSSM_TP_VERIFY_CONTEXT *RevokerVerifyContext, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR RevokerVerifyResult, CSSM_TP_CERTCHANGE_REASON Reason, CSSM_DATA_PTR NewCrlTemplate);
```
