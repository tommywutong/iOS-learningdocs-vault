---
title: CSSM_CL_CertGroupFromVerifiedBundle
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_cl_certgroupfromverifiedbundle
source_url: 'https://developer.apple.com/documentation/security/cssm_cl_certgroupfromverifiedbundle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_cl_certgroupfromverifiedbundle.json'
content_hash: 'sha256:56fa232494bb7137'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_CL_CertGroupFromVerifiedBundle

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_CL_CertGroupFromVerifiedBundle(CSSM_CL_HANDLE CLHandle, CSSM_CC_HANDLE CCHandle, const CSSM_CERT_BUNDLE *CertBundle, const SecAsn1Item *SignerCert, CSSM_CERTGROUP_PTR*CertGroup);
```
