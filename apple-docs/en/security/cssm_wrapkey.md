---
title: CSSM_WrapKey
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_wrapkey
source_url: 'https://developer.apple.com/documentation/security/cssm_wrapkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_wrapkey.json'
content_hash: 'sha256:8161b17fc568bd6d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_WrapKey

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_WrapKey(CSSM_CC_HANDLE CCHandle, const CSSM_ACCESS_CREDENTIALS *AccessCred, const CSSM_KEY *Key, const SecAsn1Item *DescriptiveData, CSSM_WRAP_KEY_PTR WrappedKey);
```
