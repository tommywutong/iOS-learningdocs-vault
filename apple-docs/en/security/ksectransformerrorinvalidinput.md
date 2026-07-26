---
title: kSecTransformErrorInvalidInput
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.7+（13.0 起废弃）, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksectransformerrorinvalidinput
source_url: 'https://developer.apple.com/documentation/security/ksectransformerrorinvalidinput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectransformerrorinvalidinput.json'
content_hash: 'sha256:5552c65235f19acc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTransformErrorInvalidInput

<sub>Global Variable</sub>

The input set on a transform is invalid.

<sub>Mac Catalyst, macOS</sub>

```swift
var kSecTransformErrorInvalidInput: CFIndex { get }
```

## Discussion

This can occur if the data set for an attribute does not meet certain requirements such as correct key usage for signing data.
