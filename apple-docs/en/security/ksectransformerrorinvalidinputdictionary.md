---
title: kSecTransformErrorInvalidInputDictionary
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.7+（13.0 起废弃）, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksectransformerrorinvalidinputdictionary
source_url: 'https://developer.apple.com/documentation/security/ksectransformerrorinvalidinputdictionary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectransformerrorinvalidinputdictionary.json'
content_hash: 'sha256:a6de84d30886bb79'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTransformErrorInvalidInputDictionary

<sub>Global Variable</sub>

A dictionary used to import a transform has invalid data.

<sub>Mac Catalyst, macOS</sub>

```swift
var kSecTransformErrorInvalidInputDictionary: CFIndex { get }
```

## Discussion

This error may occur when trying to import a transform from a data representation using the [SecTransformCreateFromExternalRepresentation](<sectransformcreatefromexternalrepresentation(____).md>) function.
