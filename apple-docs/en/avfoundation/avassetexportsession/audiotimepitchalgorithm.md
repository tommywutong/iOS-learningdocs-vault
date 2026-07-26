---
title: audioTimePitchAlgorithm
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetexportsession/audiotimepitchalgorithm
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/audiotimepitchalgorithm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/audiotimepitchalgorithm.json'
content_hash: 'sha256:7b1ca06e9a6fa1dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# audioTimePitchAlgorithm

<sub>Instance Property</sub>

A processing algorithm for managing audio pitch for scaled audio edits.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var audioTimePitchAlgorithm: AVAudioTimePitchAlgorithm { get set }
```

## Discussion

The default value is [AVAudioTimePitchAlgorithmSpectral](../avaudiotimepitchalgorithm/spectral.md).

## See Also

### Configuring audio output

- [audioMix](audiomix.md) — The parameters for audio mixing and an indication of whether to enable nondefault audio mixing for export.
