---
title: AVVideoEncoderSpecificationKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.10+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideoencoderspecificationkey
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideoencoderspecificationkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideoencoderspecificationkey.json'
content_hash: 'sha256:fb783cf0340773d6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoEncoderSpecificationKey

<sub>Global Variable</sub>

The video encoder specification includes options for choosing a specific video encoder.

<sub>macOS</sub>

```swift
let AVVideoEncoderSpecificationKey: String
```

## Discussion

The value for this key is a dictionary containing `kVTVideoEncoderSpecification_*` keys specified in the VideoToolbox framework. This key should be specified at the top level of an `AVVideoSettings` dictionary.
