---
title: CSSM_ModuleUnload
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_moduleunload
source_url: 'https://developer.apple.com/documentation/security/cssm_moduleunload'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_moduleunload.json'
content_hash: 'sha256:8dbf676fc34abae5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_ModuleUnload

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_ModuleUnload(const CSSM_GUID *ModuleGuid, CSSM_API_ModuleEventHandler AppNotifyCallback, void *AppNotifyCallbackCtx);
```
