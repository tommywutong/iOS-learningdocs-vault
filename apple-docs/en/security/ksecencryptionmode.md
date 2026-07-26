---
title: kSecEncryptionMode
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksecencryptionmode
source_url: 'https://developer.apple.com/documentation/security/ksecencryptionmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecencryptionmode.json'
content_hash: 'sha256:edaa65cfe901030f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecEncryptionMode

<sub>Global Variable</sub>

The encryption mode.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
let kSecEncryptionMode: CFString
```

## Discussion

If you do not supply this key, an appropriate value will be supplied for you. See [Encryption Modes](transform-attributes.md#Encryption-Modes) for a list of possible values.
