---
title: SecKeyGetCSPHandle
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/seckeygetcsphandle
source_url: 'https://developer.apple.com/documentation/security/seckeygetcsphandle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeygetcsphandle.json'
content_hash: 'sha256:f44d0b29427555e2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyGetCSPHandle

<sub>Function</sub>

Returns the CSSM CSP handle for a key.

<sub>macOS</sub>

```objc
OSStatus SecKeyGetCSPHandle(SecKeyRef keyRef, CSSM_CSP_HANDLE *cspHandle);
```

## Parameters

- `keyRef` — The key for which you want a CSSM CSP handle.

- `cspHandle` — On return, points to the CSSM CSP handle for the specified key. This pointer remains valid until the key reference is released. Do not attempt to modify or free this data.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

A CSSM CSP handle is required as an input to a number of CSSM functions.
