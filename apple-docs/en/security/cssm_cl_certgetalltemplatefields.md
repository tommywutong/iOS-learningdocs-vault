---
title: CSSM_CL_CertGetAllTemplateFields
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_cl_certgetalltemplatefields
source_url: 'https://developer.apple.com/documentation/security/cssm_cl_certgetalltemplatefields'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_cl_certgetalltemplatefields.json'
content_hash: 'sha256:6575a8b9ac85e769'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_CL_CertGetAllTemplateFields

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_CL_CertGetAllTemplateFields(CSSM_CL_HANDLE CLHandle, const SecAsn1Item *CertTemplate, uint32 *NumberOfFields, CSSM_FIELD_PTR*CertFields);
```
