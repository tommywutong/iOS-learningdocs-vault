---
title: CSSM_DecryptData
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_decryptdata
source_url: 'https://developer.apple.com/documentation/security/cssm_decryptdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_decryptdata.json'
content_hash: 'sha256:9d16020eed189185'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_DecryptData

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_DecryptData(CSSM_CC_HANDLE CCHandle, const SecAsn1Item *CipherBufs, uint32 CipherBufCount, CSSM_DATA_PTR ClearBufs, uint32 ClearBufCount, CSSM_SIZE *bytesDecrypted, CSSM_DATA_PTR RemData);
```
