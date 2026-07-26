---
title: CSSM_GenerateKeyP
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_generatekeyp
source_url: 'https://developer.apple.com/documentation/security/cssm_generatekeyp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_generatekeyp.json'
content_hash: 'sha256:925d6c719641c790'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_GenerateKeyP

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_GenerateKeyP(CSSM_CC_HANDLE CCHandle, uint32 KeyUsage, uint32 KeyAttr, const SecAsn1Item *KeyLabel, const CSSM_RESOURCE_CONTROL_CONTEXT *CredAndAclEntry, CSSM_KEY_PTR Key, CSSM_PRIVILEGE Privilege);
```
