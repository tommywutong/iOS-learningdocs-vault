---
title: kSecTransformActionAttributeNotification
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksectransformactionattributenotification
source_url: 'https://developer.apple.com/documentation/security/ksectransformactionattributenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectransformactionattributenotification.json'
content_hash: 'sha256:d754c653991c08ba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTransformActionAttributeNotification

<sub>Global Variable</sub>

An action that triggers when an attribute is set.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
let kSecTransformActionAttributeNotification: CFString
```

## Discussion

Allows a block to be called when an attribute is set. This allows for caching the value as a block variable in the instance block or transmogrifying the data to be set. This action is where a custom transform would be able to do processing outside of processing input to output as process data does. One the data has been processed the action block can call SecTransformCustomSetAttribute to update and other attribute.
