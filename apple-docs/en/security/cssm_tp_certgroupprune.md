---
title: CSSM_TP_CertGroupPrune
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_tp_certgroupprune
source_url: 'https://developer.apple.com/documentation/security/cssm_tp_certgroupprune'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_tp_certgroupprune.json'
content_hash: 'sha256:3d65a39074348a98'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_TP_CertGroupPrune

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_TP_CertGroupPrune(CSSM_TP_HANDLE TPHandle, CSSM_CL_HANDLE CLHandle, const CSSM_DL_DB_LIST *DBList, const CSSM_CERTGROUP *OrderedCertGroup, CSSM_CERTGROUP_PTR*PrunedCertGroup);
```
