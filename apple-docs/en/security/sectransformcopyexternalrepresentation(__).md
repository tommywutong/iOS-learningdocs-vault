---
title: 'SecTransformCopyExternalRepresentation(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sectransformcopyexternalrepresentation(_:)'
source_url: 'https://developer.apple.com/documentation/security/sectransformcopyexternalrepresentation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformcopyexternalrepresentation%28_%3A%29.json'
content_hash: 'sha256:10099ce00a0bb228'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTransformCopyExternalRepresentation(_:)

<sub>Function</sub>

Creates a dictionary that contains enough information to be able to recreate a transform.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
func SecTransformCopyExternalRepresentation(_ transformRef: SecTransform) -> CFDictionary
```

## Parameters

- `transformRef` — The transformRef to be externalized.

## Discussion

This function returns a CFDictionaryRef that contains sufficient information to be able to recreate this transform. You can pass this CFDictionaryRef to SecTransformCreateFromExternalRepresentation to be able to recreate the transform. The dictionary can also be written out to disk using the techniques described here.

http://developer.apple.com/mac/library/documentation/CoreFoundation/Conceptual/CFPropertyLists/Articles/Saving.html
