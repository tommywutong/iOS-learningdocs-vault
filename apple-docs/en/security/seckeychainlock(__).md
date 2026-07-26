---
title: 'SecKeychainLock(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainlock(_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainlock(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainlock%28_%3A%29.json'
content_hash: 'sha256:41c2d02caaa7fb4b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainLock(_:)

<sub>Function</sub>

Locks a keychain.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainLock(_ keychain: SecKeychain?) -> OSStatus
```

## Parameters

- `keychain` — A reference to the keychain to lock. Pass `NULL` to lock the default keychain.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md). The result code [errSecNoSuchKeychain](errsecnosuchkeychain.md) indicates that specified keychain could not be found. The result code [errSecInvalidKeychain](errsecinvalidkeychain.md) indicates that the specified keychain is invalid.

## Discussion

Your application should not call this function unless you are responding to a user’s request to lock a keychain. In general, you should leave the keychain unlocked so that the user does not have to unlock it again in another application.
