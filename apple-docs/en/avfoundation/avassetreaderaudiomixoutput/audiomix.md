---
title: audioMix
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreaderaudiomixoutput/audiomix
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput/audiomix'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderaudiomixoutput/audiomix.json'
content_hash: 'sha256:c220015b1e383a95'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderAudioMixOutput](../avassetreaderaudiomixoutput.md)

# audioMix

<sub>Instance Property</sub>

The audio mix to use with this output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying var audioMix: AVAudioMix? { get set }
```

## Discussion

Use an audio mix to specify how an audio track’s volume changes over the media’s timeline.

## See Also

### Configuring audio settings

- [audioTimePitchAlgorithm](audiotimepitchalgorithm.md) — The processing algorithm to use for scaled audio edits.
