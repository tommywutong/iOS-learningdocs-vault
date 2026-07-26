---
title: kSecAttrIsPermanent
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrispermanent
source_url: 'https://developer.apple.com/documentation/security/ksecattrispermanent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrispermanent.json'
content_hash: 'sha256:5b622c0ab3614473'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrIsPermanent

<sub>Global Variable</sub>

A key whose value indicates the item’s permanence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrIsPermanent: CFString
```

## Discussion

The corresponding value is of type [CFBoolean](../corefoundation/cfboolean.md) and indicates whether or not this cryptographic key or key pair should be stored in the default keychain at creation time.

On key creation, if not explicitly specified, this attribute defaults to [kCFBooleanFalse](../corefoundation/kcfbooleanfalse.md).
