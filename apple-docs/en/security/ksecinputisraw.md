---
title: kSecInputIsRaw
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksecinputisraw
source_url: 'https://developer.apple.com/documentation/security/ksecinputisraw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecinputisraw.json'
content_hash: 'sha256:ca08629b1e755464'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecInputIsRaw

<sub>Global Variable</sub>

The input is raw.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
let kSecInputIsRaw: CFString
```

## Discussion

Using this type of input can be cryptographically unsafe (for example if you don’t blind a DSA or ECDSA signature you give away the key very quickly). You are strongly discouraged from using it..
