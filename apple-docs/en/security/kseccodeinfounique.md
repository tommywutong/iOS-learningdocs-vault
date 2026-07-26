---
title: kSecCodeInfoUnique
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccodeinfounique
source_url: 'https://developer.apple.com/documentation/security/kseccodeinfounique'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccodeinfounique.json'
content_hash: 'sha256:8f0f328fb0cdeaaf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCodeInfoUnique

<sub>Global Variable</sub>

A key whose value is a binary number that uniquely identifies static code.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCodeInfoUnique: CFString
```

## Discussion

The value is a [CFData](../corefoundation/cfdata.md) object. This identifier can be used to recognize this specific code in the future. This identifier is tied to the current version of the code, unlike the [kSecCodeInfoIdentifier](kseccodeinfoidentifier.md) identifier, which remains stable across developer-approved updates. The algorithm used for the [kSecCodeInfoUnique](kseccodeinfounique.md) identifier may change over time. However, the identifier remains stable for existing, signed code.

This is generic information returned regardless of which [Code Signing Information Flags](code-signing-information-flags.md) you pass to the [SecCodeCopySigningInformation](<seccodecopysigninginformation(______).md>) function.
