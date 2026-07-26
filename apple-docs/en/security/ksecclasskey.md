---
title: kSecClassKey
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecclasskey
source_url: 'https://developer.apple.com/documentation/security/ksecclasskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecclasskey.json'
content_hash: 'sha256:039c313264a5acd8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecClassKey

<sub>Global Variable</sub>

The value that indicates a cryptographic key item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecClassKey: CFString
```

## Discussion

The following keychain item attributes form the composite primary key of a cryptographic key item:

- [kSecAttrAccessGroup](ksecattraccessgroup.md) (on macOS, this key only applies if you set [kSecUseDataProtectionKeychain](ksecusedataprotectionkeychain.md) or [kSecAttrSynchronizable](ksecattrsynchronizable.md) to [true](../swift/true.md))
- [kSecAttrApplicationLabel](ksecattrapplicationlabel.md)
- [kSecAttrApplicationTag](ksecattrapplicationtag.md)
- [kSecAttrEffectiveKeySize](ksecattreffectivekeysize.md)
- [kSecAttrKeyClass](ksecattrkeyclass.md)
- [kSecAttrKeySizeInBits](ksecattrkeysizeinbits.md)
- [kSecAttrKeyType](ksecattrkeytype.md)
- [kSecAttrSynchronizable](ksecattrsynchronizable.md) (on iOS 14 and newer, iOS 11 newer, and watchOS 7 and newer)

Calls to [SecItemAdd](<secitemadd(____).md>) that add a cryptographic key item with the same values for all of these attributes as an existing item result in [errSecDuplicateItem](errsecduplicateitem.md).

The following keychain item attributes apply to a cryptographic key item, and don’t form part of its composite primary key:

- [kSecAttrAccess](ksecattraccess.md) (macOS only)
- [kSecAttrAccessible](ksecattraccessible.md) (on macOS, this key only applies if you set [kSecUseDataProtectionKeychain](ksecusedataprotectionkeychain.md) or [kSecAttrSynchronizable](ksecattrsynchronizable.md) to [true](../swift/true.md))
- [kSecAttrLabel](ksecattrlabel.md)
- [kSecAttrIsPermanent](ksecattrispermanent.md)
- [kSecAttrPRF](ksecattrprf.md)
- [kSecAttrSalt](ksecattrsalt.md)
- [kSecAttrRounds](ksecattrrounds.md)
- [kSecAttrCanEncrypt](ksecattrcanencrypt.md)
- [kSecAttrCanDecrypt](ksecattrcandecrypt.md)
- [kSecAttrCanDerive](ksecattrcanderive.md)
- [kSecAttrCanSign](ksecattrcansign.md)
- [kSecAttrCanVerify](ksecattrcanverify.md)
- [kSecAttrCanWrap](ksecattrcanwrap.md)
- [kSecAttrCanUnwrap](ksecattrcanunwrap.md)
