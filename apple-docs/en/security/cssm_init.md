---
title: CSSM_Init
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_init
source_url: 'https://developer.apple.com/documentation/security/cssm_init'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_init.json'
content_hash: 'sha256:2f63e4475aa0f61f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_Init

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_Init(const CSSM_VERSION *Version, CSSM_PRIVILEGE_SCOPE Scope, const CSSM_GUID *CallerGuid, CSSM_KEY_HIERARCHY KeyHierarchy, CSSM_PVC_MODE *PvcPolicy, const void *Reserved);
```
