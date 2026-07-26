---
title: 'SecKeychainItemCopyContent(_:_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainitemcopycontent(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainitemcopycontent(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainitemcopycontent%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:692a7f0e1fda103d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainItemCopyContent(_:_:_:_:_:)

<sub>Function</sub>

Copies the data and attributes stored in the given keychain item.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainItemCopyContent(_ itemRef: SecKeychainItem, _ itemClass: UnsafeMutablePointer<SecItemClass>?, _ attrList: UnsafeMutablePointer<SecKeychainAttributeList>?, _ length: UnsafeMutablePointer<UInt32>?, _ outData: UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> OSStatus
```

## Parameters

- `itemRef` — A reference to the keychain item to modify.

- `itemClass` — On return, points to the item’s class. Pass `NULL` if it is not required. See [SecItemClass](secitemclass.md) for valid constants.

- `attrList` — On entry, the list of attributes to get in this item; on return the attributes are filled in. Pass `NULL` if you don’t need to retrieve any attributes. You must call [SecKeychainItemFreeContent](<seckeychainitemfreecontent(____).md>) when you no longer need the attributes and data.

- `length` — On return, the length of the buffer pointed to by the `outData` parameter.

- `outData` — On return, a pointer to a buffer containing the data in this item. Pass `NULL` if you don’t need this data. You must call [SecKeychainItemFreeContent](<seckeychainitemfreecontent(____).md>) when you no longer need the attributes and data.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

This function returns the data and attributes of a specific keychain item.

> [!note] Note
> For new development, where possible, you should generally use [SecItemCopyMatching](<secitemcopymatching(____).md>) to obtain the data and attributes of keychain items instead, because that function is based on Core Foundation types.

You can use the [SecKeychainSearchCopyNext](seckeychainsearchcopynext.md) function to search for a keychain item if you don’t already have the item’s reference object. To find and obtain data from a password keychain item, use the [SecKeychainFindInternetPassword](<seckeychainfindinternetpassword(______________________________).md>) or [SecKeychainFindGenericPassword](<seckeychainfindgenericpassword(________________).md>) function.

You should pair the [SecKeychainItemModifyContent](<seckeychainitemmodifycontent(________).md>) function with the `SecKeychainItemCopyContent` function when dealing with older Keychain Manager functions. The [SecKeychainItemCopyAttributesAndData](<seckeychainitemcopyattributesanddata(____________).md>) and [SecKeychainItemModifyAttributesAndData](<seckeychainitemmodifyattributesanddata(________).md>) functions handle more attributes than are supported by the old Keychain Manager; however, passing them into older calls yields an invalid attribute error.

If the keychain item data is encrypted, this function decrypts the data before returning it to you. If the calling application is not in the list of trusted applications, the user is prompted before access is allowed. If the access controls for this item do not allow decryption, the function returns the `errSecAuthFailed` result code.
