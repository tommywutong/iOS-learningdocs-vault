---
title: CSSM_CSP_CreateDeriveKeyContext
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_csp_createderivekeycontext
source_url: 'https://developer.apple.com/documentation/security/cssm_csp_createderivekeycontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_csp_createderivekeycontext.json'
content_hash: 'sha256:4c710522bfd5daa6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_CSP_CreateDeriveKeyContext

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_CSP_CreateDeriveKeyContext(CSSM_CSP_HANDLE CSPHandle, CSSM_ALGORITHMS AlgorithmID, CSSM_KEY_TYPE DeriveKeyType, uint32 DeriveKeyLengthInBits, const CSSM_ACCESS_CREDENTIALS *AccessCred, const CSSM_KEY *BaseKey, uint32 IterationCount, const SecAsn1Item *Salt, const CSSM_CRYPTO_DATA *Seed, CSSM_CC_HANDLE *NewContextHandle);
```
