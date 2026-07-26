---
title: kSecMatchItemList
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecmatchitemlist
source_url: 'https://developer.apple.com/documentation/security/ksecmatchitemlist'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecmatchitemlist.json'
content_hash: 'sha256:c94122ff9b14c675'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecMatchItemList

<sub>Global Variable</sub>

A key whose value indicates a list of items to search.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecMatchItemList: CFString
```

## Discussion

To provide your own set of items to be filtered by a search query rather than searching the keychain, specify this search key in a call to the [SecItemCopyMatching](<secitemcopymatching(____).md>) function with a value that consists of an object of type [CFArray](../corefoundation/cfarray.md) where the array contains either [SecKeychainItem](seckeychainitem.md), [SecKey](seckey.md), [SecCertificate](seccertificate.md), [SecIdentity](secidentity.md), or [CFData](../corefoundation/cfdata.md) items. The objects in the provided array must all be of the same type.

To convert from persistent item references to normal item references, specify this search key in a call to the [SecItemCopyMatching](<secitemcopymatching(____).md>) function with a value of type [CFArray](../corefoundation/cfarray.md) where the array contains one or more [CFData](../corefoundation/cfdata.md) elements (the persistent references), and a return-type key of [kSecReturnRef](ksecreturnref.md) whose value is [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md).

To delete an item identified by a transient reference, specify the [kSecMatchItemList](ksecmatchitemlist.md) search key in a call to the [SecItemDelete](<secitemdelete(__).md>) function with a reference returned by using the [kSecReturnRef](ksecreturnref.md) return type key in a previous call to the [SecItemCopyMatching](<secitemcopymatching(____).md>) or [SecItemAdd](<secitemadd(____).md>) functions.

To delete an item identified by a persistent reference, specify the [kSecMatchItemList](ksecmatchitemlist.md) search key in a call to the [SecItemDelete](<secitemdelete(__).md>) function with a persistent reference returned by using the [kSecReturnPersistentRef](ksecreturnpersistentref.md) return type key to the [SecItemCopyMatching](<secitemcopymatching(____).md>) or [SecItemAdd](<secitemadd(____).md>) functions.
