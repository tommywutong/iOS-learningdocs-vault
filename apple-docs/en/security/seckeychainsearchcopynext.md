---
title: SecKeychainSearchCopyNext
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/seckeychainsearchcopynext
source_url: 'https://developer.apple.com/documentation/security/seckeychainsearchcopynext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainsearchcopynext.json'
content_hash: 'sha256:fd28dcfc873ca1e3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainSearchCopyNext

<sub>Function</sub>

Finds the next keychain item matching the given search criteria.

> [!warning] Deprecated
> Use [SecItemCopyMatching](<secitemcopymatching(____).md>) to conduct keychain item searches.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecKeychainSearchCopyNext(SecKeychainSearchRef searchRef, SecKeychainItemRef*itemRef);
```

## Parameters

- `searchRef` — A reference to the current search criteria. The search object is created in the [SecKeychainSearchCreateFromAttributes](seckeychainsearchcreatefromattributes.md) function and must be released by calling the `CFRelease` function when you are done with it.

- `itemRef` — On return, a pointer to a keychain item object of the next matching keychain item, if any. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

> [!important] Important
> This function is deprecated. The common security services manager module is no longer used.

Each item stored in the keychain contains data (such as a certificate), which is indexed by the item’s attributes. Use the [SecKeychainSearchCreateFromAttributes](seckeychainsearchcreatefromattributes.md) function to specify attributes to search for. If the `SecKeychainSearchCopyNext` function finds a match, you can use the [SecKeychainItemCopyAttributesAndData](<seckeychainitemcopyattributesanddata(____________).md>) function to retrieve the item’s data.

A [SecKeychainItem](seckeychainitem.md) object for a certificate that is stored in a keychain can be safely cast to a [SecCertificate](seccertificate.md) for use with the Certificate, Key, and Trust API.

To find and obtain data from a password keychain item, use the [SecKeychainFindInternetPassword](<seckeychainfindinternetpassword(______________________________).md>) or [SecKeychainFindGenericPassword](<seckeychainfindgenericpassword(________________).md>) function.
