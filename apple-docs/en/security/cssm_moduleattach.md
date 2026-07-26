---
title: CSSM_ModuleAttach
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_moduleattach
source_url: 'https://developer.apple.com/documentation/security/cssm_moduleattach'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_moduleattach.json'
content_hash: 'sha256:da17d05d90655736'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_ModuleAttach

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_ModuleAttach(const CSSM_GUID *ModuleGuid, const CSSM_VERSION *Version, const CSSM_API_MEMORY_FUNCS *MemoryFuncs, uint32 SubserviceID, CSSM_SERVICE_TYPE SubServiceType, CSSM_ATTACH_FLAGS AttachFlags, CSSM_KEY_HIERARCHY KeyHierarchy, CSSM_FUNC_NAME_ADDR *FunctionTable, uint32 NumFunctionTable, const void *Reserved, CSSM_MODULE_HANDLE_PTR NewModuleHandle);
```
