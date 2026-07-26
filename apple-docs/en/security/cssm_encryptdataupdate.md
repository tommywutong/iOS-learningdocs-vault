---
title: CSSM_EncryptDataUpdate
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_encryptdataupdate
source_url: 'https://developer.apple.com/documentation/security/cssm_encryptdataupdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_encryptdataupdate.json'
content_hash: 'sha256:55750a9fbf90a650'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_EncryptDataUpdate

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_EncryptDataUpdate(CSSM_CC_HANDLE CCHandle, const SecAsn1Item *ClearBufs, uint32 ClearBufCount, CSSM_DATA_PTR CipherBufs, uint32 CipherBufCount, CSSM_SIZE *bytesEncrypted);
```
