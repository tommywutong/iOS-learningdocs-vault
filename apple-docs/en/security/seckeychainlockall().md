---
title: SecKeychainLockAll()
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/seckeychainlockall()
source_url: 'https://developer.apple.com/documentation/security/seckeychainlockall()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainlockall%28%29.json'
content_hash: 'sha256:f2f62f3b1be5cbd8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainLockAll()

<sub>Function</sub>

Locks all keychains belonging to the current user.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainLockAll() -> OSStatus
```

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

Your application should not call this function unless you are responding to a user’s request to lock a keychain. In general, you should leave the keychain unlocked so that the user does not have to unlock it again in another application.
