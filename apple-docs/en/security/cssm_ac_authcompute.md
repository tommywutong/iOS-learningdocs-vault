---
title: CSSM_AC_AuthCompute
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_ac_authcompute
source_url: 'https://developer.apple.com/documentation/security/cssm_ac_authcompute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_ac_authcompute.json'
content_hash: 'sha256:446d9daa3ec1f586'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_AC_AuthCompute

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_AC_AuthCompute(CSSM_AC_HANDLE ACHandle, const CSSM_TUPLEGROUP *BaseAuthorizations, const CSSM_TUPLEGROUP *Credentials, uint32 NumberOfRequestors, const CSSM_LIST *Requestors, const CSSM_LIST *RequestedAuthorizationPeriod, const CSSM_LIST *RequestedAuthorization, CSSM_TUPLEGROUP_PTR AuthorizationResult);
```
