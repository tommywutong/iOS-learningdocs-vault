---
title: kSecAttrCanWrap
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrcanwrap
source_url: 'https://developer.apple.com/documentation/security/ksecattrcanwrap'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrcanwrap.json'
content_hash: 'sha256:2b4113f7df74b790'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrCanWrap

<sub>Global Variable</sub>

A key whose value is a Boolean that indicates whether the cryptographic key can be used for wrapping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrCanWrap: CFString
```

## Discussion

The corresponding value is of type [CFBoolean](../corefoundation/cfboolean.md) and indicates whether this cryptographic key can be used to wrap another key.

On key creation, if not explicitly specified, this attribute defaults to [kCFBooleanFalse](../corefoundation/kcfbooleanfalse.md) for private keys and [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md) for public keys.
