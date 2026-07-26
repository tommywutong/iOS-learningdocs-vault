---
title: 'SecKeychainItemCreateFromContent(_:_:_:_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainitemcreatefromcontent(_:_:_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainitemcreatefromcontent(_:_:_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainitemcreatefromcontent%28_%3A_%3A_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:92c6aff567dceb5c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainItemCreateFromContent(_:_:_:_:_:_:_:)

<sub>Function</sub>

Creates a new keychain item from the supplied parameters.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainItemCreateFromContent(_ itemClass: SecItemClass, _ attrList: UnsafeMutablePointer<SecKeychainAttributeList>, _ length: UInt32, _ data: UnsafeRawPointer?, _ keychainRef: SecKeychain?, _ initialAccess: SecAccess?, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>?) -> OSStatus
```

## Parameters

- `itemClass` — A constant identifying the class of item to create. See [SecItemClass](secitemclass.md) for valid constants.

- `attrList` — A pointer to the list of attributes for the item to create.

- `length` — The length of the buffer pointed to by the `data` parameter.

- `data` — A pointer to a buffer containing the data to store.

- `keychainRef` — A reference to the keychain in which to add the item. Pass `NULL` to specify the default keychain.

- `initialAccess` — An access object for this keychain item. Use the [SecAccessCreate](<secaccesscreate(______).md>) function to create an access object or the [SecKeychainItemCopyAccess](<seckeychainitemcopyaccess(____).md>) function to copy an access object from another keychain item. If you pass `NULL` for this parameter, the access defaults to the application creating the item.

- `itemRef` — On return, a pointer to a reference to the newly created keychain item. This parameter is optional. You must call the `CFRelease` function to release this object when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

Each item stored in the keychain contains data (such as a certificate), which is indexed by the item’s attributes. Use this function to create a keychain item from its attributes and data. To create keychain items that hold passwords, use the [SecKeychainAddInternetPassword](<seckeychainaddinternetpassword(______________________________).md>) or [SecKeychainAddGenericPassword](<seckeychainaddgenericpassword(________________).md>) functions.

A `SecKeychainItemRef` object for a certificate that is stored in a keychain can be safely cast to a `SecCertificateRef` for use with the Certificate, Key, and Trust API.

This function automatically calls the function [SecKeychainUnlock](<seckeychainunlock(________).md>) to display the Unlock Keychain dialog box if the keychain is currently locked.
