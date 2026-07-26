---
title: 'SecKeychainItemSetAccess(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainitemsetaccess(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainitemsetaccess(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainitemsetaccess%28_%3A_%3A%29.json'
content_hash: 'sha256:24a78eeac7568c78'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainItemSetAccess(_:_:)

<sub>Function</sub>

Sets the access of a given keychain item.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainItemSetAccess(_ itemRef: SecKeychainItem, _ access: SecAccess) -> OSStatus
```

## Parameters

- `itemRef` — A keychain item.

- `access` — An access instance to replace the keychain item’s current access instance. Use the [SecAccessCreate](<secaccesscreate(______).md>) function to create a default access instance.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

Use this function to attach an access instance to a particular keychain item. Alternatively, you can use the [kSecAttrAccess](ksecattraccess.md) attribute when calling either of the [SecItemAdd](<secitemadd(____).md>) or [SecItemUpdate](<secitemupdate(____).md>) methods.
