---
title: 'SecKeychainCopyAccess(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychaincopyaccess(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychaincopyaccess(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaincopyaccess%28_%3A_%3A%29.json'
content_hash: 'sha256:01a1d7c83c63dc4e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainCopyAccess(_:_:)

<sub>Function</sub>

Retrieves the application access of a keychain.

> [!warning] Deprecated
> This function is not implemented and returns an [errSecUnimplemented](errsecunimplemented.md) error code if called.

<sub>macOS</sub>

```swift
func SecKeychainCopyAccess(_ keychain: SecKeychain?, _ access: UnsafeMutablePointer<SecAccess?>) -> OSStatus
```

## Parameters

- `keychain` — A reference to the keychain from which to copy the access object. Pass `NULL` to specify the default keychain.

- `access` — A pointer to an access object. On return, this points to the access object of the specified keychain.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).
