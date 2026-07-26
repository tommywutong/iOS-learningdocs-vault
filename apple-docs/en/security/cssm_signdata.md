---
title: CSSM_SignData
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_signdata
source_url: 'https://developer.apple.com/documentation/security/cssm_signdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_signdata.json'
content_hash: 'sha256:d5ae7fb858b370db'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_SignData

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_SignData(CSSM_CC_HANDLE CCHandle, const SecAsn1Item *DataBufs, uint32 DataBufCount, CSSM_ALGORITHMS DigestAlgorithm, CSSM_DATA_PTR Signature);
```
