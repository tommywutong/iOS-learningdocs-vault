---
title: CSSM_TP_PassThrough
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_tp_passthrough
source_url: 'https://developer.apple.com/documentation/security/cssm_tp_passthrough'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_tp_passthrough.json'
content_hash: 'sha256:f0abb6524dc041ef'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_TP_PassThrough

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_TP_PassThrough(CSSM_TP_HANDLE TPHandle, CSSM_CL_HANDLE CLHandle, CSSM_CC_HANDLE CCHandle, const CSSM_DL_DB_LIST *DBList, uint32 PassThroughId, const void *InputParams, void **OutputParams);
```
