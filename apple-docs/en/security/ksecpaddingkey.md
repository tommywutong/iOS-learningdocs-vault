---
title: kSecPaddingKey
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksecpaddingkey
source_url: 'https://developer.apple.com/documentation/security/ksecpaddingkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecpaddingkey.json'
content_hash: 'sha256:73fd4255c4495a06'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecPaddingKey

<sub>Global Variable</sub>

The kind of padding to use.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
let kSecPaddingKey: CFString
```

## Discussion

If you do not supply a value for this key, an appropriate value will be supplied for you. See [Padding Types](transform-attributes.md#Padding-Types) for a list of valid values.
