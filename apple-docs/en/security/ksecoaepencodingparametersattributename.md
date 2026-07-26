---
title: kSecOAEPEncodingParametersAttributeName
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksecoaepencodingparametersattributename
source_url: 'https://developer.apple.com/documentation/security/ksecoaepencodingparametersattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecoaepencodingparametersattributename.json'
content_hash: 'sha256:d15627ee4b5c74ba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecOAEPEncodingParametersAttributeName

<sub>Global Variable</sub>

The OAEP encoding parameters.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
let kSecOAEPEncodingParametersAttributeName: CFString
```

## Discussion

Set this value to a [CFData](../corefoundation/cfdata.md) object when the [kSecPaddingKey](ksecpaddingkey.md) attribute is set to [kSecPaddingOAEPKey](ksecpaddingoaepkey.md). If you don’t set this attribute, a zero length data object is used by default.

This attribute is ignored when padding is not set to OAEP.
