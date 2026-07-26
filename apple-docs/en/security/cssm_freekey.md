---
title: CSSM_FreeKey
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_freekey
source_url: 'https://developer.apple.com/documentation/security/cssm_freekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_freekey.json'
content_hash: 'sha256:3b65d398c5399024'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_FreeKey

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_FreeKey(CSSM_CSP_HANDLE CSPHandle, const CSSM_ACCESS_CREDENTIALS *AccessCred, CSSM_KEY_PTR KeyPtr, CSSM_BOOL Delete);
```
