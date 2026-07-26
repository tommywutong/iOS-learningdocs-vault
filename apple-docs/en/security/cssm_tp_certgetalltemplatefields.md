---
title: CSSM_TP_CertGetAllTemplateFields
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_tp_certgetalltemplatefields
source_url: 'https://developer.apple.com/documentation/security/cssm_tp_certgetalltemplatefields'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_tp_certgetalltemplatefields.json'
content_hash: 'sha256:ad4da39d62ac7c47'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_TP_CertGetAllTemplateFields

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_TP_CertGetAllTemplateFields(CSSM_TP_HANDLE TPHandle, CSSM_CL_HANDLE CLHandle, const SecAsn1Item *CertTemplate, uint32 *NumberOfFields, CSSM_FIELD_PTR*CertFields);
```
