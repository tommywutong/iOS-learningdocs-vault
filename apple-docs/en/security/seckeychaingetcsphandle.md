---
title: SecKeychainGetCSPHandle
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/seckeychaingetcsphandle
source_url: 'https://developer.apple.com/documentation/security/seckeychaingetcsphandle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaingetcsphandle.json'
content_hash: 'sha256:ce6dd4bf3dc9887b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainGetCSPHandle

<sub>Function</sub>

Returns the CSSM CSP handle for the given keychain object.

> [!warning] Deprecated
> The common security services manager module is no longer used.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecKeychainGetCSPHandle(SecKeychainRef keychain, CSSM_CSP_HANDLE *cspHandle);
```

## Parameters

- `keychain` — A keychain object.

- `cspHandle` — On return, a pointer to the CSSM CSP handle for the given keychain. The handle is valid until the keychain object is released.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

> [!important] Important
> This function is deprecated. The common security services manager module is no longer used.
