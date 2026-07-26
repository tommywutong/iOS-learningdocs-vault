---
title: CSSM_TP_FormSubmit
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_tp_formsubmit
source_url: 'https://developer.apple.com/documentation/security/cssm_tp_formsubmit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_tp_formsubmit.json'
content_hash: 'sha256:5e3b3a418453b0ae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_TP_FormSubmit

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_TP_FormSubmit(CSSM_TP_HANDLE TPHandle, CSSM_TP_FORM_TYPE FormType, const SecAsn1Item *Form, const CSSM_TP_AUTHORITY_ID *ClearanceAuthority, const CSSM_TP_AUTHORITY_ID *RepresentedAuthority, CSSM_ACCESS_CREDENTIALS_PTR Credentials);
```
