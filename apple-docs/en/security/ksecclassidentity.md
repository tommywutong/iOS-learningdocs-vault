---
title: kSecClassIdentity
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecclassidentity
source_url: 'https://developer.apple.com/documentation/security/ksecclassidentity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecclassidentity.json'
content_hash: 'sha256:15d891b15885d9d9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecClassIdentity

<sub>Global Variable</sub>

The value that indicates an identity item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecClassIdentity: CFString
```

## Discussion

An identity is a certificate paired with its associated private key. Keychain services stores the certificate and the private key separately; it represents the pair as an identity if the certificate’s [kSecAttrPublicKeyHash](ksecattrpublickeyhash.md) attribute matches the key’s [kSecAttrApplicationLabel](ksecattrapplicationlabel.md) attribute.

Because an identity is the combination of a private key and a certificate, this class shares attributes of both [kSecClassKey](ksecclasskey.md) and [kSecClassCertificate](ksecclasscertificate.md). Multiple certificates can all attest the identity of the same private key, so the attributes that form an identity’s composite primary key are the same as those for a certificate.

The set of identity items available to your app in the keychain can change without explicitly adding, updating, or deleting identity items. For example, if the keychain contains a cryptographic key item and certificate item that form an identity and you delete the key, the identity no longer exists.
