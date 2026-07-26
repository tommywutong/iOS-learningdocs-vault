---
title: CSSM_TP_CertGroupConstruct
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_tp_certgroupconstruct
source_url: 'https://developer.apple.com/documentation/security/cssm_tp_certgroupconstruct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_tp_certgroupconstruct.json'
content_hash: 'sha256:407c4f863257c60e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_TP_CertGroupConstruct

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_TP_CertGroupConstruct(CSSM_TP_HANDLE TPHandle, CSSM_CL_HANDLE CLHandle, CSSM_CSP_HANDLE CSPHandle, const CSSM_DL_DB_LIST *DBList, const void *ConstructParams, const CSSM_CERTGROUP *CertGroupFrag, CSSM_CERTGROUP_PTR*CertGroup);
```
