---
title: AVAudioTimePitchAlgorithm
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avaudiotimepitchalgorithm
source_url: 'https://developer.apple.com/documentation/avfoundation/avaudiotimepitchalgorithm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avaudiotimepitchalgorithm.json'
content_hash: 'sha256:5ef040662e129af5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAudioTimePitchAlgorithm

<sub>Structure</sub>

An algorithm used to set the audio pitch as the rate changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AVAudioTimePitchAlgorithm
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type properties

- [AVAudioTimePitchAlgorithmLowQualityZeroLatency](avaudiotimepitchalgorithm/lowqualityzerolatency.md) — A low-quality and very low computationally intensive pitch algorithm. _(deprecated)_
- [AVAudioTimePitchAlgorithmSpectral](avaudiotimepitchalgorithm/spectral.md) — A highest-quality time pitch algorithm that’s suitable for music.
- [AVAudioTimePitchAlgorithmTimeDomain](avaudiotimepitchalgorithm/timedomain.md) — A modest quality time pitch algorithm that’s suitable for voice.
- [AVAudioTimePitchAlgorithmVarispeed](avaudiotimepitchalgorithm/varispeed.md) — A high-quality time pitch algorithm that doesn’t perform pitch correction.

### Initializers

- [init(rawValue:)](<avaudiotimepitchalgorithm/init(rawvalue_).md>) — Creates a new time pitch algorithm with a string.

## See Also

### Getting the time pitch algorithm setting

- [audioTimePitchAlgorithm](avaudiomixinputparameters/audiotimepitchalgorithm.md) — The processing algorithm used to manage audio pitch for scaled audio edits.
