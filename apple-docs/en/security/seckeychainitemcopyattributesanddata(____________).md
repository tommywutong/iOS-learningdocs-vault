---
title: 'SecKeychainItemCopyAttributesAndData(_:_:_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainitemcopyattributesanddata(_:_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainitemcopyattributesanddata(_:_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainitemcopyattributesanddata%28_%3A_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:90f3f37aba527a11'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainItemCopyAttributesAndData(_:_:_:_:_:_:)

<sub>Function</sub>

Retrieves the data and/or attributes stored in the given keychain item.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainItemCopyAttributesAndData(_ itemRef: SecKeychainItem, _ info: UnsafeMutablePointer<SecKeychainAttributeInfo>?, _ itemClass: UnsafeMutablePointer<SecItemClass>?, _ attrList: UnsafeMutablePointer<UnsafeMutablePointer<SecKeychainAttributeList>?>?, _ length: UnsafeMutablePointer<UInt32>?, _ outData: UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> OSStatus
```

## Parameters

- `itemRef` — A reference to the keychain item from which you wish to retrieve data or attributes.

- `info` — A pointer to a list of tags and formats of attributes to retrieve. You can call [SecKeychainAttributeInfoForItemID](<seckeychainattributeinfoforitemid(______).md>) to obtain a list of all possible attribute tags and formats for the item’s class. Pass `NULL` if you don’t wish to retrieve any attributes.

- `itemClass` — On return, the item’s class. Pass `NULL` if not required. See [SecItemClass](secitemclass.md) for valid constants.

- `attrList` — On return, the retrieved attributes and their values .  Pass `NULL` if not required. You must call the function [SecKeychainItemFreeAttributesAndData](<seckeychainitemfreeattributesanddata(____).md>) when you no longer need the attributes and values.

- `length` — On return, the actual length of the data returned in the `outData` parameter.

- `outData` — On return, the data in this item. Pass `NULL` if not required. You must call the function [SecKeychainItemFreeAttributesAndData](<seckeychainitemfreeattributesanddata(____).md>) when you no longer need the data.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

This function returns the data and attributes of a specific keychain item.

> [!note] Note
> This is a CSSM-based API. CSSM is deprecated.
>
> For new development, where possible, you should generally use [SecItemCopyMatching](<secitemcopymatching(____).md>) to obtain attributes of keychain items instead, because that function is based on Core Foundation types.

You can use the [SecKeychainSearchCopyNext](seckeychainsearchcopynext.md) function to search for a keychain item if you don’t already have the item’s reference object. To find and obtain data from a password keychain item, use the [SecKeychainFindInternetPassword](<seckeychainfindinternetpassword(______________________________).md>) or [SecKeychainFindGenericPassword](<seckeychainfindgenericpassword(________________).md>) function.

You should pair the `SecKeychainItemCopyAttributesAndData` function with the [SecKeychainItemModifyAttributesAndData](<seckeychainitemmodifyattributesanddata(________).md>) function, as these functions handle more attributes than are support by the old Keychain Manager and passing them into older calls yields an invalid attribute error. Use the functions [SecKeychainItemModifyContent](<seckeychainitemmodifycontent(________).md>) and [SecKeychainItemCopyContent](<seckeychainitemcopycontent(__________).md>) when dealing with older Keychain Manager functions.

If the keychain item data is encrypted, this function decrypts the data before returning it to you. If the calling application is not in the list of trusted applications, the user is prompted before access is allowed. If the access controls for this item do not allow decryption, the function returns the `errSecAuthFailed` result code.
