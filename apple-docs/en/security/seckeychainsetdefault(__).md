---
title: 'SecKeychainSetDefault(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainsetdefault(_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainsetdefault(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainsetdefault%28_%3A%29.json'
content_hash: 'sha256:e69f84154b47c663'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainSetDefault(_:)

<sub>Function</sub>

Sets the default keychain.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainSetDefault(_ keychain: SecKeychain?) -> OSStatus
```

## Parameters

- `keychain` — A reference to the keychain you wish to make the default.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md). The result code [errSecNoSuchKeychain](errsecnosuchkeychain.md) indicates that the specified keychain could not be found. The result code [errSecInvalidKeychain](errsecinvalidkeychain.md) indicates that the specified keychain is invalid.

## Discussion

In most cases, your application should not need to set the default keychain, because this is a choice normally made by the user. You may call this function to change where a password or other keychain items are added, but since this is a user choice, you should set the default keychain back to the user specified keychain when you are done.
