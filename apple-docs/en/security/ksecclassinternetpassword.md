---
title: kSecClassInternetPassword
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecclassinternetpassword
source_url: 'https://developer.apple.com/documentation/security/ksecclassinternetpassword'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecclassinternetpassword.json'
content_hash: 'sha256:e0979b74f6457651'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecClassInternetPassword

<sub>Global Variable</sub>

The value that indicates an Internet password item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecClassInternetPassword: CFString
```

## Discussion

The following keychain item attributes form the composite primary key of an Internet password item:

- [kSecAttrAccessGroup](ksecattraccessgroup.md) (on macOS, this key only applies if you set [kSecUseDataProtectionKeychain](ksecusedataprotectionkeychain.md) or [kSecAttrSynchronizable](ksecattrsynchronizable.md) to [true](../swift/true.md))
- [kSecAttrAccount](ksecattraccount.md)
- [kSecAttrAuthenticationType](ksecattrauthenticationtype.md)
- [kSecAttrPath](ksecattrpath.md)
- [kSecAttrPort](ksecattrport.md)
- [kSecAttrProtocol](ksecattrprotocol.md)
- [kSecAttrSecurityDomain](ksecattrsecuritydomain.md)
- [kSecAttrServer](ksecattrserver.md)
- [kSecAttrSynchronizable](ksecattrsynchronizable.md)

Calls to [SecItemAdd](<secitemadd(____).md>) that add an Internet password item with the same values for all of these attributes as an existing item result in [errSecDuplicateItem](errsecduplicateitem.md).

The following keychain item attributes apply to an Internet password item, and don’t form part of its composite primary key:

- [kSecAttrAccess](ksecattraccess.md) (macOS only)
- [kSecAttrAccessible](ksecattraccessible.md) (on macOS, this key only applies if you set [kSecUseDataProtectionKeychain](ksecusedataprotectionkeychain.md) or [kSecAttrSynchronizable](ksecattrsynchronizable.md) to [true](../swift/true.md))
- [kSecAttrCreationDate](ksecattrcreationdate.md)
- [kSecAttrModificationDate](ksecattrmodificationdate.md)
- [kSecAttrDescription](ksecattrdescription.md)
- [kSecAttrComment](ksecattrcomment.md)
- [kSecAttrCreator](ksecattrcreator.md)
- [kSecAttrType](ksecattrtype.md)
- [kSecAttrLabel](ksecattrlabel.md)
- [kSecAttrIsInvisible](ksecattrisinvisible.md)
- [kSecAttrIsNegative](ksecattrisnegative.md)
