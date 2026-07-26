---
title: CSSM_TP_RetrieveCredResult
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_tp_retrievecredresult
source_url: 'https://developer.apple.com/documentation/security/cssm_tp_retrievecredresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_tp_retrievecredresult.json'
content_hash: 'sha256:38ae40528af978f4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_TP_RetrieveCredResult

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_TP_RetrieveCredResult(CSSM_TP_HANDLE TPHandle, const SecAsn1Item *ReferenceIdentifier, const CSSM_TP_CALLERAUTH_CONTEXT *CallerAuthCredentials, sint32 *EstimatedTime, CSSM_BOOL *ConfirmationRequired, CSSM_TP_RESULT_SET_PTR*RetrieveOutput);
```
