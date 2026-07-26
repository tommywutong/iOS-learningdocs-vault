---
title: SecExternalItemType
framework: Security
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secexternalitemtype
source_url: 'https://developer.apple.com/documentation/security/secexternalitemtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secexternalitemtype.json'
content_hash: 'sha256:6b94ac8e7f130ca7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecExternalItemType

<sub>Enumeration</sub>

The import item type.

<sub>macOS</sub>

```swift
enum SecExternalItemType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kSecItemTypeUnknown](secexternalitemtype/itemtypeunknown.md) — Indicates that the caller does not know the type of information being imported or exported.
- [kSecItemTypePrivateKey](secexternalitemtype/itemtypeprivatekey.md) — Indicates a private key.
- [kSecItemTypePublicKey](secexternalitemtype/itemtypepublickey.md) — Indicates a public key.
- [kSecItemTypeSessionKey](secexternalitemtype/itemtypesessionkey.md) — Indicates a session key.
- [kSecItemTypeCertificate](secexternalitemtype/itemtypecertificate.md) — Indicates a certificate.
- [kSecItemTypeAggregate](secexternalitemtype/itemtypeaggregate.md) — Indicates a set of certificates or certificates and private keys.

### Initializers

- [init(rawValue:)](<secexternalitemtype/init(rawvalue_).md>)
