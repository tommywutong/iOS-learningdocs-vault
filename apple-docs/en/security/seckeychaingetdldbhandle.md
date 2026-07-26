---
title: SecKeychainGetDLDBHandle
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/seckeychaingetdldbhandle
source_url: 'https://developer.apple.com/documentation/security/seckeychaingetdldbhandle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaingetdldbhandle.json'
content_hash: 'sha256:ffe7d90442bd220a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainGetDLDBHandle

<sub>Function</sub>

Returns the CSSM database handle for a given keychain object.

> [!warning] Deprecated
> The common security services manager module is no longer used.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecKeychainGetDLDBHandle(SecKeychainRef keychain, CSSM_DL_DB_HANDLE *dldbHandle);
```

## Parameters

- `keychain` — A keychain object.

- `dldbHandle` — On return, a pointer to the CSSM database handle for the given keychain. The handle is valid until the keychain object is released.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

> [!important] Important
> This function is deprecated. The common security services manager module is no longer used.
