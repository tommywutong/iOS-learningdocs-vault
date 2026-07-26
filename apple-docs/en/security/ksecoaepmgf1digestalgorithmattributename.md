---
title: kSecOAEPMGF1DigestAlgorithmAttributeName
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksecoaepmgf1digestalgorithmattributename
source_url: 'https://developer.apple.com/documentation/security/ksecoaepmgf1digestalgorithmattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecoaepmgf1digestalgorithmattributename.json'
content_hash: 'sha256:d60cabe524910ef5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecOAEPMGF1DigestAlgorithmAttributeName

<sub>Global Variable</sub>

The OAEP MGF1 digest algorithm.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
let kSecOAEPMGF1DigestAlgorithmAttributeName: CFString
```

## Discussion

Set this value to one of the digest algorithms listed in [Digest Types](transform-attributes.md#Digest-Types) when the [kSecPaddingKey](ksecpaddingkey.md) attribute is set to [kSecPaddingOAEPKey](ksecpaddingoaepkey.md). If you don’t set this attribute, [kSecDigestSHA1](ksecdigestsha1.md) is used by default.

This attribute is ignored when padding is not set to OAEP.
