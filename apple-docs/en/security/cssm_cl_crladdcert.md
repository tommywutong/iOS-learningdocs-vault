---
title: CSSM_CL_CrlAddCert
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_cl_crladdcert
source_url: 'https://developer.apple.com/documentation/security/cssm_cl_crladdcert'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_cl_crladdcert.json'
content_hash: 'sha256:39d518aa60d594eb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_CL_CrlAddCert

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_CL_CrlAddCert(CSSM_CL_HANDLE CLHandle, CSSM_CC_HANDLE CCHandle, const SecAsn1Item *Cert, uint32 NumberOfFields, const CSSM_FIELD *CrlEntryFields, const SecAsn1Item *OldCrl, CSSM_DATA_PTR NewCrl);
```
