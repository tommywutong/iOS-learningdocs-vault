---
title: keyAttributes
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secitemimportexportkeyparameters/keyattributes
source_url: 'https://developer.apple.com/documentation/security/secitemimportexportkeyparameters/keyattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemimportexportkeyparameters/keyattributes.json'
content_hash: 'sha256:b00deb9a2a2152a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecItemImportExportKeyParameters](../secitemimportexportkeyparameters.md)

# keyAttributes

<sub>Instance Property</sub>

An array containing zero or more key attributes for an imported key.

<sub>macOS</sub>

```swift
var keyAttributes: Unmanaged<CFArray>?
```

## Discussion

Valid values are [kSecAttrIsPermanent](../ksecattrispermanent.md), [kSecAttrIsSensitive](../ksecattrissensitive.md), and [kSecAttrIsExtractable](../ksecattrisextractable.md). If you set this attribute array to `NULL`, the following defaults are used:

- The item is marked permanent if a keychain is specified.
- The item is marked sensitive if it is a private key.
- The item is marked extractable by default.
