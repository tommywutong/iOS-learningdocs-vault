---
title: CSSM_DigestData
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_digestdata
source_url: 'https://developer.apple.com/documentation/security/cssm_digestdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_digestdata.json'
content_hash: 'sha256:09f03bfba89ef7d8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_DigestData

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_DigestData(CSSM_CC_HANDLE CCHandle, const SecAsn1Item *DataBufs, uint32 DataBufCount, CSSM_DATA_PTR Digest);
```
