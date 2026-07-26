---
title: kSecAttrAccess
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattraccess
source_url: 'https://developer.apple.com/documentation/security/ksecattraccess'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattraccess.json'
content_hash: 'sha256:f561857943d42735'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrAccess

<sub>Global Variable</sub>

A key with a value that indicates access control list settings for the item.

<sub>macOS</sub>

```swift
let kSecAttrAccess: CFString
```

## Discussion

The corresponding value is a [SecAccess](secaccess.md) instance that describes the access control settings for this item. Create an access instance by calling the [SecAccessCreate](<secaccesscreate(______).md>) method. For more information, see [Access Control Lists](access-control-lists.md).

Use this attribute to set an access instance when you:

- Create a keychain item, by adding the `kSecAttrAccess` key to the dictionary you pass to [SecItemAdd](<secitemadd(____).md>).
- Modify a keychain item, by adding the `kSecAttrAccess` key to the dictionary you pass as the second parameter to [SecItemUpdate](<secitemupdate(____).md>).

You can’t use this attribute to:

- Search for an item by its access instance; for example, by adding `kSecAttrAccess` to the dictionary you pass as the first parameter to [SecItemUpdate](<secitemupdate(____).md>). [SecItemUpdate](<secitemupdate(____).md>) and [SecItemCopyMatching](<secitemcopymatching(____).md>) ignore this key when searching for keychain items.
- Get an item’s access instance with [SecItemCopyMatching](<secitemcopymatching(____).md>). To get an item’s access instance, call [SecKeychainItemCopyAccess](<seckeychainitemcopyaccess(____).md>).

> [!important] Important
> This attribute is mutually exclusive with the [kSecAttrAccessControl](ksecattraccesscontrol.md) attribute. Also, it only applies to keychain items stored in macOS that don’t have one or both of the [kSecAttrSynchronizable](ksecattrsynchronizable.md) or [kSecUseDataProtectionKeychain](ksecusedataprotectionkeychain.md) keys set to `true`. For information on access control for other keychain items, see [Sharing access to keychain items among a collection of apps](sharing-access-to-keychain-items-among-a-collection-of-apps.md).
