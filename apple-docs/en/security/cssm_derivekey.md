---
title: CSSM_DeriveKey
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_derivekey
source_url: 'https://developer.apple.com/documentation/security/cssm_derivekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_derivekey.json'
content_hash: 'sha256:e9253b775157c093'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_DeriveKey

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_DeriveKey(CSSM_CC_HANDLE CCHandle, CSSM_DATA_PTR Param, uint32 KeyUsage, uint32 KeyAttr, const SecAsn1Item *KeyLabel, const CSSM_RESOURCE_CONTROL_CONTEXT *CredAndAclEntry, CSSM_KEY_PTR DerivedKey);
```
