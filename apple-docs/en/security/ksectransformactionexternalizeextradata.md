---
title: kSecTransformActionExternalizeExtraData
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksectransformactionexternalizeextradata
source_url: 'https://developer.apple.com/documentation/security/ksectransformactionexternalizeextradata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectransformactionexternalizeextradata.json'
content_hash: 'sha256:9d8b771393926de2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTransformActionExternalizeExtraData

<sub>Global Variable</sub>

An action that triggers after data is stored.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
let kSecTransformActionExternalizeExtraData: CFString
```

## Discussion

Allows for adding to the data that is stored using an override to the kSecTransformActionExternalizeExtraData block. The output of this override is a dictionary that contains the custom externalized data. A common use of this override is to write out a version number of a custom transform.
