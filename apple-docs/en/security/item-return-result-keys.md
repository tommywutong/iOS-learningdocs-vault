---
title: Item return result keys
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/item-return-result-keys
source_url: 'https://developer.apple.com/documentation/security/item-return-result-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/item-return-result-keys.json'
content_hash: 'sha256:a6f3fffa548cb719'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Keychain services](keychain-services.md) · [Keychain items](keychain-items.md)

# Item return result keys

<sub>API Collection</sub>

Specify how you want returned keychain item data formatted.

## Overview

When you use one of the [SecItemAdd](<secitemadd(____).md>) or [SecItemCopyMatching](<secitemcopymatching(____).md>) functions to add or search for keychain items, these functions return the item’s data and attributes through the `result` parameter to which you provide a pointer. Use the item result keys described below in the corresponding query dictionary to indicate how those results should be formatted:

- If you request a data reference with [kSecReturnRef](ksecreturnref.md), the search returns a reference of type [SecKeychainItem](seckeychainitem.md), [SecKey](seckey.md), [SecCertificate](seccertificate.md), [SecIdentity](secidentity.md), or [CFData](../corefoundation/cfdata.md), depending on the class of the item.
- If you request a persistent data reference using [kSecReturnPersistentRef](ksecreturnpersistentref.md), the search returns an item reference of type [CFData](../corefoundation/cfdata.md) that you can store on disk or pass between processes. You later convert persistent references to regular references with another call to the [SecItemCopyMatching](<secitemcopymatching(____).md>) function, using an array of persistent references (of the same item class) as the value for the [kSecMatchItemList](ksecmatchitemlist.md) key.
- If you ask for the data itself with [kSecReturnData](ksecreturndata.md), the search returns a [CFData](../corefoundation/cfdata.md) instance that holds the actual data. This is typically what you want for password items. To undo the encryption it added prior to storing the item, keychain services decrypts the data before returning it to you. Don’t use [kSecReturnData](ksecreturndata.md) for cryptographic key or identity items, as the key material may not be extractable. Instead, call [SecKeyCopyExternalRepresentation](<seckeycopyexternalrepresentation(____).md>), and check the `error` parameter if it returns `nil`.
- If you request the item’s attributes using [kSecReturnAttributes](ksecreturnattributes.md) or more than one return type, the search returns a dictionary. Item attributes are represented directly as key-value pairs in this dictionary, while the item’s data appears in one or more of the previously mentioned forms, and is associated with the appropriate item value type key from [Item return result keys](item-return-result-keys.md).
- When you specify a match limit greater than one, the search produces an array. Each element of the array is itself a search result formatted according to the previous rules.

## Topics

### Item result keys

- [kSecReturnData](ksecreturndata.md) — A key whose value is a Boolean that indicates whether or not to return item data.
- [kSecReturnAttributes](ksecreturnattributes.md) — A key whose value is a Boolean indicating whether or not to return item attributes.
- [kSecReturnRef](ksecreturnref.md) — A key whose value is a Boolean indicating whether or not to return a reference to an item.
- [kSecReturnPersistentRef](ksecreturnpersistentref.md) — A key whose value is a Boolean indicating whether or not to return a persistent reference to an item.

### Item value type keys

- [kSecValueData](ksecvaluedata.md) — A key whose value is the item’s data.
- [kSecValueRef](ksecvalueref.md) — A key whose value is a reference to the item.
- [kSecValuePersistentRef](ksecvaluepersistentref.md) — A key whose value is a persistent reference to the item.
