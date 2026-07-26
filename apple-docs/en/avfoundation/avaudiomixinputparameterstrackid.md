---
title: AVAudioMixInputParametersTrackID
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avaudiomixinputparameterstrackid
source_url: 'https://developer.apple.com/documentation/avfoundation/avaudiomixinputparameterstrackid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avaudiomixinputparameterstrackid.json'
content_hash: 'sha256:326a218dd1efc109'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAudioMixInputParametersTrackID

<sub>Enumeration</sub>

Special value for the trackID property of AVAudioMixInputParameters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum AVAudioMixInputParametersTrackID
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a track identifier

- [init(rawValue:)](<avaudiomixinputparameterstrackid/init(rawvalue_).md>) _(beta)_

### Track identifiers

- [AVAudioMixInputParametersTrackMixID](avaudiomixinputparameterstrackid/mixid.md) — Indicates that the specified input parameters should be applied to the mix of all audio tracks rather than to a single specific audio track. This is particularly useful for setting up volume ramps or an audio tap for streaming playback. _(beta)_

## See Also

### Mixing

- [AVAudioMix](avaudiomix.md) — An object that manages the input parameters for mixing audio tracks.
- [AVAudioMixInputParameters](avaudiomixinputparameters.md) — An object that represents the parameters that you apply when adding an audio track to a mix.
- [AVMutableAudioMix](avmutableaudiomix.md) — An object that manages the input parameters for mixing audio tracks.
- [AVMutableAudioMixInputParameters](avmutableaudiomixinputparameters.md) — The parameters you use when adding an audio track to a mix.
