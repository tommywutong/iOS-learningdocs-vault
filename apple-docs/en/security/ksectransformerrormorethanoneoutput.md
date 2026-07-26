---
title: kSecTransformErrorMoreThanOneOutput
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.7+（13.0 起废弃）, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksectransformerrormorethanoneoutput
source_url: 'https://developer.apple.com/documentation/security/ksectransformerrormorethanoneoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectransformerrormorethanoneoutput.json'
content_hash: 'sha256:a6e21679cf3cc561'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTransformErrorMoreThanOneOutput

<sub>Global Variable</sub>

A transform has an internal routing error that has caused multiple outputs instead of a single discrete output.

<sub>Mac Catalyst, macOS</sub>

```swift
var kSecTransformErrorMoreThanOneOutput: CFIndex { get }
```

## Discussion

This error occurs if [SecTransformExecute](<sectransformexecute(____).md>) has already been called.
