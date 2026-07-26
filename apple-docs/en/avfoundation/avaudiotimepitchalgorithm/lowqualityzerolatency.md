---
title: lowQualityZeroLatency
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+（15.0 起废弃）, iPadOS 7.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, tvOS 9.0+（15.0 起废弃）, watchOS 1.0+（8.0 起废弃）]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avaudiotimepitchalgorithm/lowqualityzerolatency
source_url: 'https://developer.apple.com/documentation/avfoundation/avaudiotimepitchalgorithm/lowqualityzerolatency'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avaudiotimepitchalgorithm/lowqualityzerolatency.json'
content_hash: 'sha256:b3823b31975a9144'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAudioTimePitchAlgorithm](../avaudiotimepitchalgorithm.md)

# lowQualityZeroLatency

<sub>Type Property</sub>

A low-quality and very low computationally intensive pitch algorithm.

> [!warning] Deprecated
> Use [AVAudioTimePitchAlgorithmTimeDomain](timedomain.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, watchOS</sub>

```swift
static let lowQualityZeroLatency: AVAudioTimePitchAlgorithm
```

## Discussion

This algorithm is suitable for brief fast-forward and rewind effects, as well as low-quality voice. The rate snaps to `{0.5, 0.666667, 0.8, 1.0, 1.25, 1.5, 2.0}`.

## See Also

### Constants

- [AVAudioTimePitchAlgorithmTimeDomain](timedomain.md) — A modest quality time pitch algorithm that’s suitable for voice.
- [AVAudioTimePitchAlgorithmVarispeed](varispeed.md) — A high-quality time pitch algorithm that doesn’t perform pitch correction.
- [AVAudioTimePitchAlgorithmSpectral](spectral.md) — A highest-quality time pitch algorithm that’s suitable for music.
