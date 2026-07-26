---
title: CSSM_WrapKeyP
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_wrapkeyp
source_url: 'https://developer.apple.com/documentation/security/cssm_wrapkeyp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_wrapkeyp.json'
content_hash: 'sha256:6796fb201a3d164d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_WrapKeyP

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_WrapKeyP(CSSM_CC_HANDLE CCHandle, const CSSM_ACCESS_CREDENTIALS *AccessCred, const CSSM_KEY *Key, const SecAsn1Item *DescriptiveData, CSSM_WRAP_KEY_PTR WrappedKey, CSSM_PRIVILEGE Privilege);
```
