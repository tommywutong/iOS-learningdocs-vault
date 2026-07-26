---
title: Item class keys and values
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/item-class-keys-and-values
source_url: 'https://developer.apple.com/documentation/security/item-class-keys-and-values'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/item-class-keys-and-values.json'
content_hash: 'sha256:93432248e0492860'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Keychain services](keychain-services.md) · [Keychain items](keychain-items.md)

# Item class keys and values

<sub>API Collection</sub>

Specify the class of a keychain item.

## Overview

Keychain items come in a variety of classes according to the kind of data they hold, such as passwords, cryptographic keys, and certificates. The item’s class dictates which attributes apply and enables the system to decide whether to encrypt the data. For example, the system encrypts passwords, but not certificates because they aren’t secret.

Use the key and one of the corresponding values listed here to specify the class for a new item you create with a call to the [SecItemAdd](<secitemadd(____).md>) function by placing the key/value pair in the `attributes` dictionary.

Later, use this same pair in the `query` dictionary when searching for an item with one of the [SecItemCopyMatching](<secitemcopymatching(____).md>), [SecItemUpdate](<secitemupdate(____).md>), or [SecItemDelete](<secitemdelete(__).md>) functions.

## Topics

### Item class keys

- [kSecClass](ksecclass.md) — A dictionary key whose value is the item’s class.

### Item class values

- [kSecClassGenericPassword](ksecclassgenericpassword.md) — The value that indicates a generic password item.
- [kSecClassInternetPassword](ksecclassinternetpassword.md) — The value that indicates an Internet password item.
- [kSecClassCertificate](ksecclasscertificate.md) — The value that indicates a certificate item.
- [kSecClassKey](ksecclasskey.md) — The value that indicates a cryptographic key item.
- [kSecClassIdentity](ksecclassidentity.md) — The value that indicates an identity item.
