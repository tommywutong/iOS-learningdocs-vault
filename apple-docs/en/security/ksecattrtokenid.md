---
title: kSecAttrTokenID
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrtokenid
source_url: 'https://developer.apple.com/documentation/security/ksecattrtokenid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrtokenid.json'
content_hash: 'sha256:7592193ab4bf93fa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrTokenID

<sub>Global Variable</sub>

A key whose value indicates that a cryptographic key is in an external store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrTokenID: CFString
```

## Discussion

The corresponding value is of type [CFString](../corefoundation/cfstring.md), and may only be one of the constants specified in [Token ID Values](item-attribute-keys-and-values.md#Token-ID-Values). Presence of this key indicates that the item is backed by an external store, as uniquely identified by the value. An item without this attribute is stored as normal in the keychain database.

> [!important] Important
> You can’t change this attribute after creating the keychain item. It isn’t possible to migrate existing items between stores. Setting `kSecAttrTokenID` when creating a keychain item in macOS makes it behave like an iOS keychain item, as if [kSecAttrSynchronizable](ksecattrsynchronizable.md) were also set.

Use this attribute only in the top-level parameter dictionary during key creation and not in one of the private or public key sub-dictionaries given by [kSecPrivateKeyAttrs](ksecprivatekeyattrs.md) or [kSecPublicKeyAttrs](ksecpublickeyattrs.md), respectively. For an example, see [Protecting keys with the Secure Enclave](protecting-keys-with-the-secure-enclave.md).
