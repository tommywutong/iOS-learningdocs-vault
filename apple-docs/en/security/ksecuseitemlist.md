---
title: kSecUseItemList
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+（12.0 起废弃）, iPadOS 2.0+（12.0 起废弃）, Mac Catalyst 2.0+（12.0 起废弃）, macOS 10.6+, tvOS 9.0+（12.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（5.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksecuseitemlist
source_url: 'https://developer.apple.com/documentation/security/ksecuseitemlist'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecuseitemlist.json'
content_hash: 'sha256:70c222480e8331cf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecUseItemList

<sub>Global Variable</sub>

A key whose value is an array of items to search.

> [!warning] Deprecated
> Not implemented on this platform

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecUseItemList: CFString
```

## Discussion

The corresponding value is of type [CFArray](../corefoundation/cfarray.md), where the array contains either [SecKeychainItem](seckeychainitem.md), [SecKey](seckey.md), [SecCertificate](seccertificate.md), [SecIdentity](secidentity.md), or  (for persistent item references) [CFData](../corefoundation/cfdata.md) items. The items in the array must all be of the same type.

When this attribute is provided, no keychains are searched. Instead, the specified array is treated as the set of all possible items to search (or to add if the function being called is [SecItemAdd](<secitemadd(____).md>)).
