---
title: CSSM_VerifyMac
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_verifymac
source_url: 'https://developer.apple.com/documentation/security/cssm_verifymac'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_verifymac.json'
content_hash: 'sha256:55db7ffa81a4d916'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_VerifyMac

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_VerifyMac(CSSM_CC_HANDLE CCHandle, const SecAsn1Item *DataBufs, uint32 DataBufCount, const SecAsn1Item *Mac);
```
