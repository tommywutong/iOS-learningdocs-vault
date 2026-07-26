---
title: 'SecKeychainItemModifyAttributesAndData(_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainitemmodifyattributesanddata(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainitemmodifyattributesanddata(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainitemmodifyattributesanddata%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:e5e0dc748d29474b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainItemModifyAttributesAndData(_:_:_:_:)

<sub>Function</sub>

Updates an existing keychain item after changing its attributes or data.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainItemModifyAttributesAndData(_ itemRef: SecKeychainItem, _ attrList: UnsafePointer<SecKeychainAttributeList>?, _ length: UInt32, _ data: UnsafeRawPointer?) -> OSStatus
```

## Parameters

- `itemRef` — A reference to the keychain item to modify.

- `attrList` — A pointer to the list of attributes to modify and their new values. Pass `NULL` if you have no need to modify attributes.

- `length` — The length of the buffer pointed to by the `data` parameter. Pass `0` if you pass `NULL` in the `data` parameter.

- `data` — A pointer to a buffer containing the data to store. Pass `NULL` if you do not need to modify the data.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

The keychain item is written to the keychain’s permanent data store. If the keychain item has not previously been added to a keychain, a call to this function does nothing and returns `noErr`.

> [!note] Note
> For new development, where possible, you should generally use [SecItemUpdate](<secitemupdate(____).md>) to obtain attributes of keychain items instead, because that function is based on Core Foundation types.

Note that when you use this function to modify a keychain item, Keychain Services updates the modification date of the item. Therefore, you cannot use this function to modify the modification date, as the value you specify will be overwritten with the current time. If you want to change the modification date to something other than the current time, use a CSSM function to do so.

You should pair the [SecKeychainItemCopyAttributesAndData](<seckeychainitemcopyattributesanddata(____________).md>) function with the `SecKeychainItemModifyAttributesAndData` function, as these functions handle more attributes than are support by the old Keychain Manager and passing them into older calls yields an invalid attribute error. Use the functions [SecKeychainItemModifyContent](<seckeychainitemmodifycontent(________).md>) and [SecKeychainItemCopyContent](<seckeychainitemcopycontent(__________).md>) when dealing with older Keychain Manager functions.
