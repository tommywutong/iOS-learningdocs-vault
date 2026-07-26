---
title: kSecTransformActionAttributeValidation
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksectransformactionattributevalidation
source_url: 'https://developer.apple.com/documentation/security/ksectransformactionattributevalidation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectransformactionattributevalidation.json'
content_hash: 'sha256:910832ff6641ab31'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTransformActionAttributeValidation

<sub>Global Variable</sub>

An action that triggers to perform validation of an attribute.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
let kSecTransformActionAttributeValidation: CFString
```

## Discussion

Allows a block to be called to validate the new value for an attribute. The default is no validation and any CFTypeRef can be used as the new value. The block should return NULL if the value is ok to set on the attribute or a CFErrorRef otherwise.
