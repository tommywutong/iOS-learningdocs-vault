---
title: 'SecKeychainItemCreateCopy(_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainitemcreatecopy(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainitemcreatecopy(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainitemcreatecopy%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:9951db9d945f2f32'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainItemCreateCopy(_:_:_:_:)

<sub>Function</sub>

Copies a keychain item from one keychain to another.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainItemCreateCopy(_ itemRef: SecKeychainItem, _ destKeychainRef: SecKeychain?, _ initialAccess: SecAccess?, _ itemCopy: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus
```

## Parameters

- `itemRef` — A reference to the keychain item to copy.

- `destKeychainRef` — A reference to the keychain in which to insert the copied keychain item. Pass `NULL` to specify the default keychain.

- `initialAccess` — The initial access for the copied keychain item. Use the [SecAccessCreate](<secaccesscreate(______).md>) function to create an access object or the [SecKeychainItemCopyAccess](<seckeychainitemcopyaccess(____).md>) function to copy an access object from another keychain item. If you pass `NULL` for this parameter, the access defaults to the application creating the item.

- `itemCopy` — On return, a pointer to a copy of the keychain item referenced by the `itemRef` parameter. You must call the `CFRelease` function to release this object when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).
