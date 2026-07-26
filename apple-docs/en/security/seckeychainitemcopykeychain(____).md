---
title: 'SecKeychainItemCopyKeychain(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainitemcopykeychain(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainitemcopykeychain(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainitemcopykeychain%28_%3A_%3A%29.json'
content_hash: 'sha256:3503cb8e65e248b2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainItemCopyKeychain(_:_:)

<sub>Function</sub>

Returns the keychain object of a given keychain item.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainItemCopyKeychain(_ itemRef: SecKeychainItem, _ keychainRef: UnsafeMutablePointer<SecKeychain?>) -> OSStatus
```

## Parameters

- `itemRef` — A keychain item object.

- `keychainRef` — On return, a pointer to a keychain object referencing the given keychain item. You must call the `CFRelease` function to release this object when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).
