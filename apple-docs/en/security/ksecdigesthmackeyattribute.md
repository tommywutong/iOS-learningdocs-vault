---
title: kSecDigestHMACKeyAttribute
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksecdigesthmackeyattribute
source_url: 'https://developer.apple.com/documentation/security/ksecdigesthmackeyattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecdigesthmackeyattribute.json'
content_hash: 'sha256:19d40c04eb82d696'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecDigestHMACKeyAttribute

<sub>Global Variable</sub>

The key for HMAC operation.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
let kSecDigestHMACKeyAttribute: CFString
```

## Discussion

The value is a [CFData](../corefoundation/cfdata.md) object that specifies the key when [kSecDigestTypeAttribute](ksecdigesttypeattribute.md) attribute is set to one of the HMAC options listed in [Digest Types](transform-attributes.md#Digest-Types). If this value is not set, the transform will assume a zero length key.
