---
title: kSecCodeInfoIdentifier
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccodeinfoidentifier
source_url: 'https://developer.apple.com/documentation/security/kseccodeinfoidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccodeinfoidentifier.json'
content_hash: 'sha256:00d344f07d77a4e9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCodeInfoIdentifier

<sub>Global Variable</sub>

A key whose value is the signing identifier sealed into the signature.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCodeInfoIdentifier: CFString
```

## Discussion

The value is a [CFString](../corefoundation/cfstring.md) object. Absent for unsigned code.

This is generic information returned regardless of which [Code Signing Information Flags](code-signing-information-flags.md) you pass to the [SecCodeCopySigningInformation](<seccodecopysigninginformation(______).md>) function.
