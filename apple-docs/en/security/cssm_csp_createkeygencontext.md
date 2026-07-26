---
title: CSSM_CSP_CreateKeyGenContext
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_csp_createkeygencontext
source_url: 'https://developer.apple.com/documentation/security/cssm_csp_createkeygencontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_csp_createkeygencontext.json'
content_hash: 'sha256:1b87ecd306c8b118'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_CSP_CreateKeyGenContext

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_CSP_CreateKeyGenContext(CSSM_CSP_HANDLE CSPHandle, CSSM_ALGORITHMS AlgorithmID, uint32 KeySizeInBits, const CSSM_CRYPTO_DATA *Seed, const SecAsn1Item *Salt, const CSSM_DATE *StartDate, const CSSM_DATE *EndDate, const SecAsn1Item *Params, CSSM_CC_HANDLE *NewContextHandle);
```
