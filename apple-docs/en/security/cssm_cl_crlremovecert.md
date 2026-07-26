---
title: CSSM_CL_CrlRemoveCert
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_cl_crlremovecert
source_url: 'https://developer.apple.com/documentation/security/cssm_cl_crlremovecert'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_cl_crlremovecert.json'
content_hash: 'sha256:90f16f1a02c4e404'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_CL_CrlRemoveCert

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_CL_CrlRemoveCert(CSSM_CL_HANDLE CLHandle, const SecAsn1Item *Cert, const SecAsn1Item *OldCrl, CSSM_DATA_PTR NewCrl);
```
