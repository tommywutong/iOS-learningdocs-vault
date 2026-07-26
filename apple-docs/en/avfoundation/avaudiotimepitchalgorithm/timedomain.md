---
title: timeDomain
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avaudiotimepitchalgorithm/timedomain
source_url: 'https://developer.apple.com/documentation/avfoundation/avaudiotimepitchalgorithm/timedomain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avaudiotimepitchalgorithm/timedomain.json'
content_hash: 'sha256:343b7e06f39d86c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAudioTimePitchAlgorithm](../avaudiotimepitchalgorithm.md)

# timeDomain

<sub>Type Property</sub>

A modest quality time pitch algorithm that’s suitable for voice.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let timeDomain: AVAudioTimePitchAlgorithm
```

## Discussion

This is less computationally intensive than [AVAudioTimePitchAlgorithmSpectral](spectral.md), and uses a variable rate from `1/32` to `32`.

## See Also

### Constants

- [AVAudioTimePitchAlgorithmVarispeed](varispeed.md) — A high-quality time pitch algorithm that doesn’t perform pitch correction.
- [AVAudioTimePitchAlgorithmSpectral](spectral.md) — A highest-quality time pitch algorithm that’s suitable for music.
- [AVAudioTimePitchAlgorithmLowQualityZeroLatency](lowqualityzerolatency.md) — A low-quality and very low computationally intensive pitch algorithm. _(deprecated)_
