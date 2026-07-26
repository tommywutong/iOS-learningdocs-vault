---
title: kSecPaddingOAEPKey
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.8+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksecpaddingoaepkey
source_url: 'https://developer.apple.com/documentation/security/ksecpaddingoaepkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecpaddingoaepkey.json'
content_hash: 'sha256:2bd344c0ecfea3f4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecPaddingOAEPKey

<sub>Global Variable</sub>

PKCS7 padding will be used when encrypting or decrypting.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
let kSecPaddingOAEPKey: CFString
```

## Discussion

When using this padding type, consider also setting the [kSecOAEPMessageLengthAttributeName](ksecoaepmessagelengthattributename.md), [kSecOAEPEncodingParametersAttributeName](ksecoaepencodingparametersattributename.md), and [kSecOAEPMGF1DigestAlgorithmAttributeName](ksecoaepmgf1digestalgorithmattributename.md) attributes.
