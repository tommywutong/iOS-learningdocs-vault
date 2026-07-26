---
title: CSSM_TP_ConfirmCredResult
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_tp_confirmcredresult
source_url: 'https://developer.apple.com/documentation/security/cssm_tp_confirmcredresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_tp_confirmcredresult.json'
content_hash: 'sha256:a623db41e37daacf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_TP_ConfirmCredResult

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_TP_ConfirmCredResult(CSSM_TP_HANDLE TPHandle, const SecAsn1Item *ReferenceIdentifier, const CSSM_TP_CALLERAUTH_CONTEXT *CallerAuthCredentials, const CSSM_TP_CONFIRM_RESPONSE *Responses, const CSSM_TP_AUTHORITY_ID *PreferredAuthority);
```
