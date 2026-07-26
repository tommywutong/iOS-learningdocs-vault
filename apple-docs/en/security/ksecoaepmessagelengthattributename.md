---
title: kSecOAEPMessageLengthAttributeName
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksecoaepmessagelengthattributename
source_url: 'https://developer.apple.com/documentation/security/ksecoaepmessagelengthattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecoaepmessagelengthattributename.json'
content_hash: 'sha256:8c16e0594dde9ca5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecOAEPMessageLengthAttributeName

<sub>Global Variable</sub>

The OAEP message length.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
let kSecOAEPMessageLengthAttributeName: CFString
```

## Discussion

Optionally set the value to a [CFNumber](../corefoundation/cfnumber.md) indicating a specific message size when the [kSecPaddingKey](ksecpaddingkey.md) attribute is set to [kSecPaddingOAEPKey](ksecpaddingoaepkey.md). If you don’t set this attribute, the minimum padding is used by default.

This attribute is ignored when padding is not set to OAEP.
