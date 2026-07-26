---
title: kSecDigestLengthAttribute
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksecdigestlengthattribute
source_url: 'https://developer.apple.com/documentation/security/ksecdigestlengthattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecdigestlengthattribute.json'
content_hash: 'sha256:2da3422e86379abb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecDigestLengthAttribute

<sub>Global Variable</sub>

The digest length.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
let kSecDigestLengthAttribute: CFString
```

## Discussion

The value is a [CFNumber](../corefoundation/cfnumber.md) that contains the digest length.
