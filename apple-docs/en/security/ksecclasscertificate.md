---
title: kSecClassCertificate
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecclasscertificate
source_url: 'https://developer.apple.com/documentation/security/ksecclasscertificate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecclasscertificate.json'
content_hash: 'sha256:1e186e88da56dc9d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecClassCertificate

<sub>Global Variable</sub>

The value that indicates a certificate item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecClassCertificate: CFString
```

## Discussion

The following keychain item attributes form the composite primary key of a certificate password item:

- [kSecAttrAccessGroup](ksecattraccessgroup.md) (on macOS, this key only applies if you set [kSecUseDataProtectionKeychain](ksecusedataprotectionkeychain.md) or [kSecAttrSynchronizable](ksecattrsynchronizable.md) to [true](../swift/true.md))
- [kSecAttrCertificateType](ksecattrcertificatetype.md)
- [kSecAttrIssuer](ksecattrissuer.md)
- [kSecAttrSerialNumber](ksecattrserialnumber.md)
- [kSecAttrSynchronizable](ksecattrsynchronizable.md) (on iOS 14 and newer, iOS 11 newer, and watchOS 7 and newer)

Calls to [SecItemAdd](<secitemadd(____).md>) that add a certificate item with the same values for all of these attributes as an existing item result in [errSecDuplicateItem](errsecduplicateitem.md).

The following keychain item attributes apply to a certificate item, and don’t form part of its composite primary key:

- [kSecAttrAccess](ksecattraccess.md) (macOS only)
- [kSecAttrAccessible](ksecattraccessible.md) (on macOS, this key only applies if you set [kSecUseDataProtectionKeychain](ksecusedataprotectionkeychain.md) or [kSecAttrSynchronizable](ksecattrsynchronizable.md) to [true](../swift/true.md))
- [kSecAttrCertificateEncoding](ksecattrcertificateencoding.md)
- [kSecAttrLabel](ksecattrlabel.md)
- [kSecAttrSubject](ksecattrsubject.md)
- [kSecAttrSubjectKeyID](ksecattrsubjectkeyid.md)
- [kSecAttrPublicKeyHash](ksecattrpublickeyhash.md)
