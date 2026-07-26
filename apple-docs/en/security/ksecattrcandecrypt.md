---
title: kSecAttrCanDecrypt
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrcandecrypt
source_url: 'https://developer.apple.com/documentation/security/ksecattrcandecrypt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrcandecrypt.json'
content_hash: 'sha256:a084c8bb02027abe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrCanDecrypt

<sub>Global Variable</sub>

A key whose value is a Boolean that indicates whether the cryptographic key can be used for decryption.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrCanDecrypt: CFString
```

## Discussion

The corresponding value is of type [CFBoolean](../corefoundation/cfboolean.md) and indicates whether this cryptographic key can be used to decrypt data.

On key creation, if not explicitly specified, this attribute defaults to [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md) for private keys and [kCFBooleanFalse](../corefoundation/kcfbooleanfalse.md) for public keys.
