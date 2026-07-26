---
title: kSecTransformActionProcessData
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksectransformactionprocessdata
source_url: 'https://developer.apple.com/documentation/security/ksectransformactionprocessdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectransformactionprocessdata.json'
content_hash: 'sha256:992e02a38bc831a2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTransformActionProcessData

<sub>Global Variable</sub>

An action that triggers to process the data of an attribute.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
let kSecTransformActionProcessData: CFString
```

## Discussion

Overrides the standard data processing for an attribute. This is almost exclusively used for processing the input attribute as the return value of their block sets the output attribute. This is used with the SecTransformOverrideAttributeAction block.
