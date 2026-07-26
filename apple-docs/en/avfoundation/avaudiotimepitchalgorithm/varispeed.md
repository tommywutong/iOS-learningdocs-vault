---
title: varispeed
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avaudiotimepitchalgorithm/varispeed
source_url: 'https://developer.apple.com/documentation/avfoundation/avaudiotimepitchalgorithm/varispeed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avaudiotimepitchalgorithm/varispeed.json'
content_hash: 'sha256:77d3b9f9da9f78fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAudioTimePitchAlgorithm](../avaudiotimepitchalgorithm.md)

# varispeed

<sub>Type Property</sub>

A high-quality time pitch algorithm that doesn’t perform pitch correction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let varispeed: AVAudioTimePitchAlgorithm
```

## Discussion

The pitch varies with the rate, and supports variable rates from `1/32` to `32`.

## See Also

### Constants

- [AVAudioTimePitchAlgorithmTimeDomain](timedomain.md) — A modest quality time pitch algorithm that’s suitable for voice.
- [AVAudioTimePitchAlgorithmSpectral](spectral.md) — A highest-quality time pitch algorithm that’s suitable for music.
- [AVAudioTimePitchAlgorithmLowQualityZeroLatency](lowqualityzerolatency.md) — A low-quality and very low computationally intensive pitch algorithm. _(deprecated)_
