---
title: CSSM_GenerateKeyPairP
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_generatekeypairp
source_url: 'https://developer.apple.com/documentation/security/cssm_generatekeypairp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_generatekeypairp.json'
content_hash: 'sha256:37561b9a550cf893'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_GenerateKeyPairP

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_GenerateKeyPairP(CSSM_CC_HANDLE CCHandle, uint32 PublicKeyUsage, uint32 PublicKeyAttr, const SecAsn1Item *PublicKeyLabel, CSSM_KEY_PTR PublicKey, uint32 PrivateKeyUsage, uint32 PrivateKeyAttr, const SecAsn1Item *PrivateKeyLabel, const CSSM_RESOURCE_CONTROL_CONTEXT *CredAndAclEntry, CSSM_KEY_PTR PrivateKey, CSSM_PRIVILEGE Privilege);
```
