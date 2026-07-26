---
title: audioTimePitchAlgorithm
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferaudiorenderer/audiotimepitchalgorithm
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/audiotimepitchalgorithm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferaudiorenderer/audiotimepitchalgorithm.json'
content_hash: 'sha256:94f0340e0b823d62'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferAudioRenderer](../avsamplebufferaudiorenderer.md)

# audioTimePitchAlgorithm

<sub>Instance Property</sub>

The processing algorithm used to manage audio pitch at different rates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var audioTimePitchAlgorithm: AVAudioTimePitchAlgorithm { get set }
```

## Discussion

The default value on iOS is [AVAudioTimePitchAlgorithmLowQualityZeroLatency](../avaudiotimepitchalgorithm/lowqualityzerolatency.md); on macOS, the default is [AVAudioTimePitchAlgorithmTimeDomain](../avaudiotimepitchalgorithm/timedomain.md). The device automatically mutes audio when [timebase](../avqueuedsamplebufferrendering/timebase.md) is not supported by [AVAudioTimePitchAlgorithm](../avaudiotimepitchalgorithm.md). Modifying this property while [timebase](../avqueuedsamplebufferrendering/timebase.md) is not `0.0` may cause the rate to briefly change to `0.0`.

## See Also

### Configuring time and pitch

- [AVAudioTimePitchAlgorithm](../avaudiotimepitchalgorithm.md) — An algorithm used to set the audio pitch as the rate changes.
