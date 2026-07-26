---
title: CSSM_CL_CertGroupToSignedBundle
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_cl_certgrouptosignedbundle
source_url: 'https://developer.apple.com/documentation/security/cssm_cl_certgrouptosignedbundle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_cl_certgrouptosignedbundle.json'
content_hash: 'sha256:fa75e3d37c6fee41'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_CL_CertGroupToSignedBundle

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_CL_CertGroupToSignedBundle(CSSM_CL_HANDLE CLHandle, CSSM_CC_HANDLE CCHandle, const CSSM_CERTGROUP *CertGroupToBundle, const CSSM_CERT_BUNDLE_HEADER *BundleInfo, CSSM_DATA_PTR SignedBundle);
```
