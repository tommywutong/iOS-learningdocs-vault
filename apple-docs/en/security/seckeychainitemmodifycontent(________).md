---
title: 'SecKeychainItemModifyContent(_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainitemmodifycontent(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainitemmodifycontent(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainitemmodifycontent%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:50f59f189f9b5ded'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainItemModifyContent(_:_:_:_:)

<sub>Function</sub>

Updates an existing keychain item after changing its attributes and/or data.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainItemModifyContent(_ itemRef: SecKeychainItem, _ attrList: UnsafePointer<SecKeychainAttributeList>?, _ length: UInt32, _ data: UnsafeRawPointer?) -> OSStatus
```

## Parameters

- `itemRef` — A reference to the keychain item to modify.

- `attrList` — A pointer to the list of attributes to set and their new values. Pass `NULL` if you have no need to modify attributes.

- `length` — The length of the buffer pointed to by the `data` parameter. Pass `0` if you pass `NULL` in the `data` parameter.

- `data` — A pointer to a buffer containing the data to store. Pass `NULL` if you do not need to modify the data.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

The keychain item is written to the keychain’s permanent data store.

> [!note] Note
> For new development, where possible, you should generally use [SecItemUpdate](<secitemupdate(____).md>) to modify the data and attributes of keychain items instead, because that function is based on Core Foundation types.

If the keychain item has not previously been added to a keychain, a call to this function does nothing and returns `noErr`.

Note that when you use this function to modify a keychain item, Keychain Services updates the modification date of the item. Therefore, you cannot use this function to modify the modification date, as the value you specify will be overwritten with the current time. If you want to change the modification date to something other than the current time, use a CSSM function to do so.

You should pair the `SecKeychainItemModifyContent` function with the [SecKeychainItemCopyContent](<seckeychainitemcopycontent(__________).md>) function when dealing with older Keychain Manager functions. The [SecKeychainItemCopyAttributesAndData](<seckeychainitemcopyattributesanddata(____________).md>) and [SecKeychainItemModifyAttributesAndData](<seckeychainitemmodifyattributesanddata(________).md>) functions handle more attributes than are support by the old Keychain Manager; however, passing them into older calls yields an invalid attribute error.
