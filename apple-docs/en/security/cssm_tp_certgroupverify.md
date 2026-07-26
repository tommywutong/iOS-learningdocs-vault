---
title: CSSM_TP_CertGroupVerify
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_tp_certgroupverify
source_url: 'https://developer.apple.com/documentation/security/cssm_tp_certgroupverify'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_tp_certgroupverify.json'
content_hash: 'sha256:e91fe4b6f8809217'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_TP_CertGroupVerify

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_TP_CertGroupVerify(CSSM_TP_HANDLE TPHandle, CSSM_CL_HANDLE CLHandle, CSSM_CSP_HANDLE CSPHandle, const CSSM_CERTGROUP *CertGroupToBeVerified, const CSSM_TP_VERIFY_CONTEXT *VerifyContext, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR VerifyContextResult);
```
