---
title: CSSM_TP_SubmitCredRequest
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_tp_submitcredrequest
source_url: 'https://developer.apple.com/documentation/security/cssm_tp_submitcredrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_tp_submitcredrequest.json'
content_hash: 'sha256:8be2f764279fc175'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_TP_SubmitCredRequest

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_TP_SubmitCredRequest(CSSM_TP_HANDLE TPHandle, const CSSM_TP_AUTHORITY_ID *PreferredAuthority, CSSM_TP_AUTHORITY_REQUEST_TYPE RequestType, const CSSM_TP_REQUEST_SET *RequestInput, const CSSM_TP_CALLERAUTH_CONTEXT *CallerAuthContext, sint32 *EstimatedTime, CSSM_DATA_PTR ReferenceIdentifier);
```
