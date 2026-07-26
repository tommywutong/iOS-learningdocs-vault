---
title: kSecCodeInfoFormat
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccodeinfoformat
source_url: 'https://developer.apple.com/documentation/security/kseccodeinfoformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccodeinfoformat.json'
content_hash: 'sha256:1335808a18d18947'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCodeInfoFormat

<sub>Global Variable</sub>

A key whose value is a string representing the type and format of the code in a form suitable for display to a knowledgeable user.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCodeInfoFormat: CFString
```

## Discussion

The value is a [CFString](../corefoundation/cfstring.md) object.

This is generic information returned regardless of which [Code Signing Information Flags](code-signing-information-flags.md)  you pass to the [SecCodeCopySigningInformation](<seccodecopysigninginformation(______).md>) function.
