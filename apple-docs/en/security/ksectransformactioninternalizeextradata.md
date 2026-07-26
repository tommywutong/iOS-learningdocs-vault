---
title: kSecTransformActionInternalizeExtraData
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksectransformactioninternalizeextradata
source_url: 'https://developer.apple.com/documentation/security/ksectransformactioninternalizeextradata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectransformactioninternalizeextradata.json'
content_hash: 'sha256:57e18d728b29c73f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTransformActionInternalizeExtraData

<sub>Global Variable</sub>

An action that triggers after attributes are read into a transform.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
let kSecTransformActionInternalizeExtraData: CFString
```

## Discussion

Overrides the standard processing that occurs when externalized data is used to create a transform. This is closely tied to the kSecTransformActionExternalizeExtraData override. The ‘normal’ attributes are read into the new transform and then this is called to read in the items that were written out using kSecTransformActionExternalizeExtraData override. A common use of this override would be to read in the version number of the externalized custom transform.
