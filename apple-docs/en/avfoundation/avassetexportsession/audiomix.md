---
title: audioMix
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetexportsession/audiomix
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/audiomix'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/audiomix.json'
content_hash: 'sha256:be3d8c379b06147d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# audioMix

<sub>Instance Property</sub>

The parameters for audio mixing and an indication of whether to enable nondefault audio mixing for export.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying var audioMix: AVAudioMix? { get set }
```

## Discussion

This value is key-value observable.

## See Also

### Configuring audio output

- [audioTimePitchAlgorithm](audiotimepitchalgorithm.md) — A processing algorithm for managing audio pitch for scaled audio edits.
