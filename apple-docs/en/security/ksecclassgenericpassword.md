---
title: kSecClassGenericPassword
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecclassgenericpassword
source_url: 'https://developer.apple.com/documentation/security/ksecclassgenericpassword'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecclassgenericpassword.json'
content_hash: 'sha256:2b546a206f354c03'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecClassGenericPassword

<sub>Global Variable</sub>

The value that indicates a generic password item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecClassGenericPassword: CFString
```

## Discussion

The following keychain item attributes form the composite primary key of a generic password item:

- [kSecAttrAccessGroup](ksecattraccessgroup.md) (on macOS, this key only applies if you set [kSecUseDataProtectionKeychain](ksecusedataprotectionkeychain.md) or [kSecAttrSynchronizable](ksecattrsynchronizable.md) to [true](../swift/true.md))
- [kSecAttrAccount](ksecattraccount.md)
- [kSecAttrService](ksecattrservice.md)
- [kSecAttrSynchronizable](ksecattrsynchronizable.md)

Calls to [SecItemAdd](<secitemadd(____).md>) that add a generic password item with the same values for all of these attributes as an existing item result in [errSecDuplicateItem](errsecduplicateitem.md).

The following keychain item attributes apply to a generic password item, and don’t form part of its composite primary key:

- [kSecAttrAccess](ksecattraccess.md) (macOS only)
- [kSecAttrAccessControl](ksecattraccesscontrol.md)
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
- [kSecAttrGeneric](ksecattrgeneric.md)
