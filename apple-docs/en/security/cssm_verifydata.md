---
title: CSSM_VerifyData
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_verifydata
source_url: 'https://developer.apple.com/documentation/security/cssm_verifydata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_verifydata.json'
content_hash: 'sha256:494f1c73028ea909'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_VerifyData

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_VerifyData(CSSM_CC_HANDLE CCHandle, const SecAsn1Item *DataBufs, uint32 DataBufCount, CSSM_ALGORITHMS DigestAlgorithm, const SecAsn1Item *Signature);
```
