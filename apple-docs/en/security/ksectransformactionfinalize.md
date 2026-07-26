---
title: kSecTransformActionFinalize
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksectransformactionfinalize
source_url: 'https://developer.apple.com/documentation/security/ksectransformactionfinalize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectransformactionfinalize.json'
content_hash: 'sha256:9cf97ecc9ff86558'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTransformActionFinalize

<sub>Global Variable</sub>

An action that triggers just before deleting a custom transform to enable custom cleanup operations.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
let kSecTransformActionFinalize: CFString
```

## Discussion

Overrides the standard behavior that occurs just before deleting a custom transform. This is typically overridden to allow for memory clean up of a custom transform. This is used with the SecTransformOverrideTransformAction block.
