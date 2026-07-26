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
doc_path: /documentation/avfoundation/avassetreaderaudiomixoutput/audiotimepitchalgorithm
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput/audiotimepitchalgorithm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderaudiomixoutput/audiotimepitchalgorithm.json'
content_hash: 'sha256:e774d5d66cc8d96e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderAudioMixOutput](../avassetreaderaudiomixoutput.md)

# audioTimePitchAlgorithm

<sub>Instance Property</sub>

The processing algorithm to use for scaled audio edits.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var audioTimePitchAlgorithm: AVAudioTimePitchAlgorithm { get set }
```

## Discussion

See [Time pitch algorithm settings](../time-pitch-algorithm-settings.md) for possible values. The system throws an exception if you set this property to a value other than one of the defined constants.

## See Also

### Configuring audio settings

- [audioMix](audiomix.md) — The audio mix to use with this output.
