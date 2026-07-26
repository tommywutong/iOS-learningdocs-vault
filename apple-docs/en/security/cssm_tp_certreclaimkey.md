---
title: CSSM_TP_CertReclaimKey
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_tp_certreclaimkey
source_url: 'https://developer.apple.com/documentation/security/cssm_tp_certreclaimkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_tp_certreclaimkey.json'
content_hash: 'sha256:c42bee4c1893dca4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_TP_CertReclaimKey

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_TP_CertReclaimKey(CSSM_TP_HANDLE TPHandle, const CSSM_CERTGROUP *CertGroup, uint32 CertIndex, CSSM_LONG_HANDLE KeyCacheHandle, CSSM_CSP_HANDLE CSPHandle, const CSSM_RESOURCE_CONTROL_CONTEXT *CredAndAclEntry);
```
