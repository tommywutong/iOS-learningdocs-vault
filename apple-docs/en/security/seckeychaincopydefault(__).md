---
title: 'SecKeychainCopyDefault(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychaincopydefault(_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychaincopydefault(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaincopydefault%28_%3A%29.json'
content_hash: 'sha256:1c8509a69f7b1cef'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainCopyDefault(_:)

<sub>Function</sub>

Retrieves a pointer to the default keychain.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainCopyDefault(_ keychain: UnsafeMutablePointer<SecKeychain?>) -> OSStatus
```

## Parameters

- `keychain` — On return, a pointer to the default keychain object. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md). The result code [errSecNoDefaultKeychain](errsecnodefaultkeychain.md) indicates that there is no default keychain.
