---
title: kSecCodeInfoSource
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccodeinfosource
source_url: 'https://developer.apple.com/documentation/security/kseccodeinfosource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccodeinfosource.json'
content_hash: 'sha256:c008e07fd253305f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCodeInfoSource

<sub>Global Variable</sub>

The source of the code signature used for the code object in a format suitable for display.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCodeInfoSource: CFString
```

## Discussion

The value is a [CFString](../corefoundation/cfstring.md) object. This string is for display purposes only. Don’t rely on the precise value returned.

This is generic information returned regardless of which [Code Signing Information Flags](code-signing-information-flags.md) you pass to the [SecCodeCopySigningInformation](<seccodecopysigninginformation(______).md>) function.
