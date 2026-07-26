---
title: kSecTransformActionStartingExecution
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksectransformactionstartingexecution
source_url: 'https://developer.apple.com/documentation/security/ksectransformactionstartingexecution'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectransformactionstartingexecution.json'
content_hash: 'sha256:46e846572d563365'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTransformActionStartingExecution

<sub>Global Variable</sub>

An action that triggers just before starting execution of a custom transform.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
let kSecTransformActionStartingExecution: CFString
```

## Discussion

Overrides the standard behavior that occurs just before starting execution of a custom transform. This is typically overridden to allow for initialization. This is used with the SecTransformOverrideTransformAction block.
