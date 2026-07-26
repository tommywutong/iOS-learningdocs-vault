---
title: SecKeychainItemGetDLDBHandle
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/seckeychainitemgetdldbhandle
source_url: 'https://developer.apple.com/documentation/security/seckeychainitemgetdldbhandle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainitemgetdldbhandle.json'
content_hash: 'sha256:787e7d92be5cd434'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainItemGetDLDBHandle

<sub>Function</sub>

Returns the CSSM database handle for a given keychain item object.

> [!warning] Deprecated
> The common security services manager module is no longer used.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecKeychainItemGetDLDBHandle(SecKeychainItemRef keyItemRef, CSSM_DL_DB_HANDLE *dldbHandle);
```

## Parameters

- `keyItemRef` — A keychain item object.

- `dldbHandle` — On return, a pointer to a CSSM database handle for the keychain database containing the given item. The handle is valid until the keychain item object is released.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

> [!important] Important
> This function is deprecated. The common security services manager module is no longer used.
