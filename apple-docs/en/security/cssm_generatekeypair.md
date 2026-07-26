---
title: CSSM_GenerateKeyPair
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_generatekeypair
source_url: 'https://developer.apple.com/documentation/security/cssm_generatekeypair'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_generatekeypair.json'
content_hash: 'sha256:90f13505b614c803'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_GenerateKeyPair

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_GenerateKeyPair(CSSM_CC_HANDLE CCHandle, uint32 PublicKeyUsage, uint32 PublicKeyAttr, const SecAsn1Item *PublicKeyLabel, CSSM_KEY_PTR PublicKey, uint32 PrivateKeyUsage, uint32 PrivateKeyAttr, const SecAsn1Item *PrivateKeyLabel, const CSSM_RESOURCE_CONTROL_CONTEXT *CredAndAclEntry, CSSM_KEY_PTR PrivateKey);
```
