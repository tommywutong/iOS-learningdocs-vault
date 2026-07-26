---
title: kSecAttrCanSign
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrcansign
source_url: 'https://developer.apple.com/documentation/security/ksecattrcansign'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrcansign.json'
content_hash: 'sha256:23800d68f84aa687'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrCanSign

<sub>Global Variable</sub>

A key whose value is a Boolean that indicates whether the cryptographic key can be used for digital signing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrCanSign: CFString
```

## Discussion

The corresponding value is of type [CFBoolean](../corefoundation/cfboolean.md) and indicates whether this cryptographic key can be used to create a digital signature.

On key creation, if not explicitly specified, this attribute defaults to [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md) for private keys and [kCFBooleanFalse](../corefoundation/kcfbooleanfalse.md) for public keys.
