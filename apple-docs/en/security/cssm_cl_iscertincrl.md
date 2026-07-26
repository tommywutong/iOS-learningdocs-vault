---
title: CSSM_CL_IsCertInCrl
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_cl_iscertincrl
source_url: 'https://developer.apple.com/documentation/security/cssm_cl_iscertincrl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_cl_iscertincrl.json'
content_hash: 'sha256:95e7667b58ca7a31'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_CL_IsCertInCrl

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_CL_IsCertInCrl(CSSM_CL_HANDLE CLHandle, const SecAsn1Item *Cert, const SecAsn1Item *Crl, CSSM_BOOL *CertFound);
```
