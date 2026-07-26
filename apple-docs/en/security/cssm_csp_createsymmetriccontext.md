---
title: CSSM_CSP_CreateSymmetricContext
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_csp_createsymmetriccontext
source_url: 'https://developer.apple.com/documentation/security/cssm_csp_createsymmetriccontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_csp_createsymmetriccontext.json'
content_hash: 'sha256:ded1bcbdddd3abbe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_CSP_CreateSymmetricContext

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_CSP_CreateSymmetricContext(CSSM_CSP_HANDLE CSPHandle, CSSM_ALGORITHMS AlgorithmID, CSSM_ENCRYPT_MODE Mode, const CSSM_ACCESS_CREDENTIALS *AccessCred, const CSSM_KEY *Key, const SecAsn1Item *InitVector, CSSM_PADDING Padding, void *Reserved, CSSM_CC_HANDLE *NewContextHandle);
```
