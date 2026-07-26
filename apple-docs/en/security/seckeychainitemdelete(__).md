---
title: 'SecKeychainItemDelete(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainitemdelete(_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainitemdelete(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainitemdelete%28_%3A%29.json'
content_hash: 'sha256:81c17a6ad54dbbfa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainItemDelete(_:)

<sub>Function</sub>

Deletes a keychain item from the default keychain’s permanent data store.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainItemDelete(_ itemRef: SecKeychainItem) -> OSStatus
```

## Parameters

- `itemRef` — A keychain item object of the item to delete. You must call the `CFRelease` function to release this object when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

If the keychain item has not previously been added to the keychain, this function does nothing and returns `noErr`.

Do not delete a keychain item and recreate it in order to modify it; instead, use the [SecKeychainItemModifyContent](<seckeychainitemmodifycontent(________).md>) or [SecKeychainItemModifyAttributesAndData](<seckeychainitemmodifyattributesanddata(________).md>) function to modify an existing keychain item. When you delete a keychain item, you lose any access controls and trust settings added by the user or by other applications.
