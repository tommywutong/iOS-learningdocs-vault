---
title: MDS_Initialize
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/mds_initialize
source_url: 'https://developer.apple.com/documentation/security/mds_initialize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/mds_initialize.json'
content_hash: 'sha256:cadd81a5ebd0a9c3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# MDS_Initialize

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN MDS_Initialize(const CSSM_GUID *pCallerGuid, const CSSM_MEMORY_FUNCS *pMemoryFunctions, MDS_FUNCS_PTR pDlFunctions, MDS_HANDLE *hMds);
```
