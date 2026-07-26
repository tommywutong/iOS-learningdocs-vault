---
title: 'SecKeychainSetAccess(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainsetaccess(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainsetaccess(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainsetaccess%28_%3A_%3A%29.json'
content_hash: 'sha256:231a097d9e9b1861'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainSetAccess(_:_:)

<sub>Function</sub>

Sets the application access for a keychain.

> [!warning] Deprecated
> In addition to the ACLs for individual keychain items, the keychain itself has ACLs. However, they are currently unused and this function isn’t implemented.

<sub>macOS</sub>

```swift
func SecKeychainSetAccess(_ keychain: SecKeychain?, _ access: SecAccess) -> OSStatus
```

## Parameters

- `keychain` — A reference to the keychain for which to set the access. Pass `NULL` to specify the default keychain.

- `access` — An access object of type [SecAccess](secaccess.md) containing access control lists for the keychain. See [Access Control Lists](access-control-lists.md) for more information about creating an access object.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).
