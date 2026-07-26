---
title: CSSM_CL_IsCertInCachedCrl
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_cl_iscertincachedcrl
source_url: 'https://developer.apple.com/documentation/security/cssm_cl_iscertincachedcrl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_cl_iscertincachedcrl.json'
content_hash: 'sha256:4eb9b38340be6a14'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_CL_IsCertInCachedCrl

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_CL_IsCertInCachedCrl(CSSM_CL_HANDLE CLHandle, const SecAsn1Item *Cert, CSSM_HANDLE CrlHandle, CSSM_BOOL *CertFound, CSSM_DATA_PTR CrlRecordIndex);
```
