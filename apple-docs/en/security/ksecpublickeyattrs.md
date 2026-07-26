---
title: kSecPublicKeyAttrs
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 4.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecpublickeyattrs
source_url: 'https://developer.apple.com/documentation/security/ksecpublickeyattrs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecpublickeyattrs.json'
content_hash: 'sha256:d7133046378d6fbb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecPublicKeyAttrs

<sub>Global Variable</sub>

A key whose value is a dictionary of cryptographic key attributes specific to a public key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecPublicKeyAttrs: CFString
```

## Discussion

The corresponding value is a [CFDictionary](../corefoundation/cfdictionary.md) containing key-value pairs for attributes specific to the public key to be generated.
