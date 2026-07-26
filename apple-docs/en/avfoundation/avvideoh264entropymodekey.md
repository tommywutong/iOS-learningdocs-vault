---
title: AVVideoH264EntropyModeKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideoh264entropymodekey
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideoh264entropymodekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideoh264entropymodekey.json'
content_hash: 'sha256:4f8c330107da0635'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoH264EntropyModeKey

<sub>Global Variable</sub>

The entropy encoding mode for H.264 compression.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let AVVideoH264EntropyModeKey: String
```

## Discussion

This property controls whether an H.264 encoder uses [AVVideoH264EntropyModeCAVLC](avvideoh264entropymodecavlc.md) or [AVVideoH264EntropyModeCABAC](avvideoh264entropymodecabac.md). CABAC generally gives better compression at the expense of higher computational overhead.

> [!important] Important
> The default value is encoder-specific and may change depending on other encoder settings. Set a value for this property only if the requested profile and level support it. Setting an incompatible value may result in encoding errors or a noncompliant output stream.

## See Also

### Entropy mode

- [AVVideoH264EntropyModeCABAC](avvideoh264entropymodecabac.md) — The encoder uses Context-based Adaptive Binary Arithmetic Coding.
- [AVVideoH264EntropyModeCAVLC](avvideoh264entropymodecavlc.md) — The encoder uses Context-based Adaptive Variable Length Coding.
