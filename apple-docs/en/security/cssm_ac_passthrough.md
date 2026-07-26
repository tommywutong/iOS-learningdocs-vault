---
title: CSSM_AC_PassThrough
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_ac_passthrough
source_url: 'https://developer.apple.com/documentation/security/cssm_ac_passthrough'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_ac_passthrough.json'
content_hash: 'sha256:0cd3e06a961f2b64'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_AC_PassThrough

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_AC_PassThrough(CSSM_AC_HANDLE ACHandle, CSSM_TP_HANDLE TPHandle, CSSM_CL_HANDLE CLHandle, CSSM_CC_HANDLE CCHandle, const CSSM_DL_DB_LIST *DBList, uint32 PassThroughId, const void *InputParams, void **OutputParams);
```
