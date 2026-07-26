---
title: kSecAttrProtocol
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrprotocol
source_url: 'https://developer.apple.com/documentation/security/ksecattrprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrprotocol.json'
content_hash: 'sha256:af33901d530752c4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrProtocol

<sub>Global Variable</sub>

A key whose value indicates the item’s protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrProtocol: CFString
```

## Discussion

The corresponding value is of type [CFString](../corefoundation/cfstring.md) and denotes the protocol for this item (see [Protocol Values](item-attribute-keys-and-values.md#Protocol-Values)). Items of class [kSecClassInternetPassword](ksecclassinternetpassword.md) have this attribute.

> [!note] Note
> For compatibility with earlier Keychain APIs, functions in [Keychain services](keychain-services.md) accept a [CFNumber](../corefoundation/cfnumber.md) for the protocol. The number is a 32-bit integer that encodes the protocol value as a `FourCharCode`. In your code, use a [CFString](../corefoundation/cfstring.md) with one of the values from [Protocol Values](item-attribute-keys-and-values.md#Protocol-Values) instead of a number.
