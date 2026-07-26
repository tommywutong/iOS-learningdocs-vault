---
title: SecItemClass
framework: Security
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secitemclass
source_url: 'https://developer.apple.com/documentation/security/secitemclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemclass.json'
content_hash: 'sha256:5163657b6e27a4ac'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecItemClass

<sub>Enumeration</sub>

Specifies a keychain item’s class code.

<sub>Mac Catalyst, macOS</sub>

```swift
enum SecItemClass
```

## Overview

These enumerations define constants your application can use to specify the type of the keychain item you wish to create, dispose, add, delete, update, copy, or locate. You can also use these constants with the tag constant [SecItemAttr](secitemattr.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kSecInternetPasswordItemClass](secitemclass/internetpassworditemclass.md) — Indicates that the item is an Internet password.
- [kSecGenericPasswordItemClass](secitemclass/genericpassworditemclass.md) — Indicates that the item is a generic password.
- [kSecCertificateItemClass](secitemclass/certificateitemclass.md) — Indicates that the item is an X509 certificate.
- [kSecPublicKeyItemClass](secitemclass/publickeyitemclass.md) — Indicates that the item is a public key of a public-private pair.
- [kSecPrivateKeyItemClass](secitemclass/privatekeyitemclass.md) — Indicates that the item is a private key of a public-private pair.
- [kSecSymmetricKeyItemClass](secitemclass/symmetrickeyitemclass.md) — Indicates that the item is a private key used for symmetric-key encryption.

### Initializers

- [init(rawValue:)](<secitemclass/init(rawvalue_).md>)
