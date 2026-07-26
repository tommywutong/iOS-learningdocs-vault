---
title: SecKeychainSearchCreateFromAttributes
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/seckeychainsearchcreatefromattributes
source_url: 'https://developer.apple.com/documentation/security/seckeychainsearchcreatefromattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainsearchcreatefromattributes.json'
content_hash: 'sha256:3dfc43d0ac8afa54'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainSearchCreateFromAttributes

<sub>Function</sub>

Creates a search object matching a list of zero or more attributes.

> [!warning] Deprecated
> Use [SecItemCopyMatching](<secitemcopymatching(____).md>) instead.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecKeychainSearchCreateFromAttributes(CFTypeRef keychainOrArray, SecItemClass itemClass, const SecKeychainAttributeList *attrList, SecKeychainSearchRef*searchRef);
```

## Parameters

- `keychainOrArray` — A reference to an array of keychains to search, a single keychain, or `NULL` to search the user’s current keychain search list. Use the function [SecKeychainCopySearchList](<seckeychaincopysearchlist(__).md>) to retrieve the user’s default search list.

- `itemClass` — The keychain item class. See [SecItemClass](secitemclass.md) for valid constants.

- `attrList` — A pointer to a list of zero or more keychain attribute records to match. Pass `NULL` to match any keychain attribute.

- `searchRef` — On return, a pointer to the current search object. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

> [!important] Important
> This function is deprecated. Use [SecItemCopyMatching](<secitemcopymatching(____).md>) instead.

Each item stored in the keychain contains data (such as a certificate), which is indexed by the item’s attributes. You look up an item in a keychain by its attributes. If you find a match, you can then retrieve the item’s data. Use the search object created by this function as input to the [SecKeychainSearchCopyNext](seckeychainsearchcopynext.md) function to find a keychain item and the [SecKeychainItemCopyAttributesAndData](<seckeychainitemcopyattributesanddata(____________).md>) function to retrieve the item’s data.

To find and obtain data from a password keychain item, use the [SecKeychainFindInternetPassword](<seckeychainfindinternetpassword(______________________________).md>) or [SecKeychainFindGenericPassword](<seckeychainfindgenericpassword(________________).md>) function.
