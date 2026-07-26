---
title: 'SecKeychainItemFreeContent(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainitemfreecontent(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainitemfreecontent(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainitemfreecontent%28_%3A_%3A%29.json'
content_hash: 'sha256:dcf18c35fa65cd44'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainItemFreeContent(_:_:)

<sub>Function</sub>

Releases the memory used by the keychain attribute list and the keychain data retrieved in a call to the [SecKeychainItemCopyContent](<seckeychainitemcopycontent(__________).md>) function.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainItemFreeContent(_ attrList: UnsafeMutablePointer<SecKeychainAttributeList>?, _ data: UnsafeMutableRawPointer?) -> OSStatus
```

## Parameters

- `attrList` — A pointer to the attribute list to release. Pass `NULL` if there is no attribute list to release.

- `data` — A pointer to the data buffer to release. Pass `NULL` if there is no data to release.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

Because the [SecKeychainFindInternetPassword](<seckeychainfindinternetpassword(______________________________).md>) and [SecKeychainFindGenericPassword](<seckeychainfindgenericpassword(________________).md>) functions call the [SecKeychainItemCopyContent](<seckeychainitemcopycontent(__________).md>) function, you must call `SecKeychainItemFreeContent` to release the data buffers after calls to those functions as well.

Because the `SecKeychainItemCopyContent` function does not allocate buffers until they are needed, you should not call the `SecKeychainItemFreeContent` function unless data is actually returned to you.
