---
title: 'SecKeychainItemCreatePersistentReference(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainitemcreatepersistentreference(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainitemcreatepersistentreference(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainitemcreatepersistentreference%28_%3A_%3A%29.json'
content_hash: 'sha256:79f29e21c13b9afc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainItemCreatePersistentReference(_:_:)

<sub>Function</sub>

Creates a persistent reference for a keychain item.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainItemCreatePersistentReference(_ itemRef: SecKeychainItem, _ persistentItemRef: UnsafeMutablePointer<CFData?>) -> OSStatus
```

## Parameters

- `itemRef` — A keychain item reference for the item for which you want a persistent reference.

- `persistentItemRef` — On return, a persistent reference for the keychain item. You must call the `CFRelease` function to release this object when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

Unlike normal references, a persistent reference may be stored on disk or passed between processes. You can convert a persistent reference into an ordinary keychain item reference (`SecKeychainItemRef`) by calling the [SecKeychainItemCopyFromPersistentReference](<seckeychainitemcopyfrompersistentreference(____).md>) function.
