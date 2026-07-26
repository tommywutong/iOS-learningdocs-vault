---
title: 'SecKeychainItemCopyAccess(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainitemcopyaccess(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainitemcopyaccess(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainitemcopyaccess%28_%3A_%3A%29.json'
content_hash: 'sha256:2867007a07d95dec'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainItemCopyAccess(_:_:)

<sub>Function</sub>

Retrieves the access of a given keychain item.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainItemCopyAccess(_ itemRef: SecKeychainItem, _ access: UnsafeMutablePointer<SecAccess?>) -> OSStatus
```

## Parameters

- `itemRef` — A keychain item.

- `access` — On return, points to the keychain item’s access instance. Call the [CFRelease](../corefoundation/cfrelease.md) method to release this access instance when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

Use this method to retrieve the access instance from a keychain item. Alternatively, you can look for the [kSecAttrAccess](ksecattraccess.md) attribute among the keychain item’s attributes when you call the [SecItemCopyMatching](<secitemcopymatching(____).md>) method.
