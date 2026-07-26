---
title: SecExternalFormat.formatUnknown
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secexternalformat/formatunknown
source_url: 'https://developer.apple.com/documentation/security/secexternalformat/formatunknown'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secexternalformat/formatunknown.json'
content_hash: 'sha256:699b5aa374afce51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecExternalFormat](../secexternalformat.md)

# SecExternalFormat.formatUnknown

<sub>Case</sub>

<sub>macOS</sub>

```swift
case formatUnknown
```

## Discussion

When importing, indicates the format is unknown. When exporting, use the default format for the item. For asymmetric keys, the default is `kSecFormatOpenSSL`. For symmetric keys, the default is `kSecFormatRawKey`. For certificates, the default is `kSecFormatX509Cert`. For multiple items, the default is `kSecFormatPEMSequence`.
