---
title: CSSM_UnwrapKeyP
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_unwrapkeyp
source_url: 'https://developer.apple.com/documentation/security/cssm_unwrapkeyp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_unwrapkeyp.json'
content_hash: 'sha256:bcc2a46724b66863'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_UnwrapKeyP

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_UnwrapKeyP(CSSM_CC_HANDLE CCHandle, const CSSM_KEY *PublicKey, const CSSM_WRAP_KEY *WrappedKey, uint32 KeyUsage, uint32 KeyAttr, const SecAsn1Item *KeyLabel, const CSSM_RESOURCE_CONTROL_CONTEXT *CredAndAclEntry, CSSM_KEY_PTR UnwrappedKey, CSSM_DATA_PTR DescriptiveData, CSSM_PRIVILEGE Privilege);
```
