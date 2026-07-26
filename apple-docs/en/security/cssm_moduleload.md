---
title: CSSM_ModuleLoad
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_moduleload
source_url: 'https://developer.apple.com/documentation/security/cssm_moduleload'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_moduleload.json'
content_hash: 'sha256:08bbf3fd1c097d4d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_ModuleLoad

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_ModuleLoad(const CSSM_GUID *ModuleGuid, CSSM_KEY_HIERARCHY KeyHierarchy, CSSM_API_ModuleEventHandler AppNotifyCallback, void *AppNotifyCallbackCtx);
```
