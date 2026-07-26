---
title: CSSM_CSP_CreateSignatureContext
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_csp_createsignaturecontext
source_url: 'https://developer.apple.com/documentation/security/cssm_csp_createsignaturecontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_csp_createsignaturecontext.json'
content_hash: 'sha256:053b1866228adf13'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_CSP_CreateSignatureContext

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_CSP_CreateSignatureContext(CSSM_CSP_HANDLE CSPHandle, CSSM_ALGORITHMS AlgorithmID, const CSSM_ACCESS_CREDENTIALS *AccessCred, const CSSM_KEY *Key, CSSM_CC_HANDLE *NewContextHandle);
```
