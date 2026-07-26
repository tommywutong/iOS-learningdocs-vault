---
title: 'SecKeychainItemCopyFromPersistentReference(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainitemcopyfrompersistentreference(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainitemcopyfrompersistentreference(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainitemcopyfrompersistentreference%28_%3A_%3A%29.json'
content_hash: 'sha256:8d37537448f8acf8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainItemCopyFromPersistentReference(_:_:)

<sub>Function</sub>

Provides a keychain item reference, given a persistent reference.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainItemCopyFromPersistentReference(_ persistentItemRef: CFData, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus
```

## Parameters

- `persistentItemRef` — A persistent reference for a keychain item.

- `itemRef` — On return, a keychain item reference for the item for which you provided a persistent reference. You must call the `CFRelease` function to release this object when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

A persistent reference may be stored on disk or passed between processes. You use the [SecKeychainItemCreatePersistentReference](<seckeychainitemcreatepersistentreference(____).md>) function to create a persistent reference.
