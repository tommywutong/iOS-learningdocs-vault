---
title: AVMutableAudioMixInputParameters
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutableaudiomixinputparameters
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutableaudiomixinputparameters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutableaudiomixinputparameters.json'
content_hash: 'sha256:46079a4f7c1c19ab'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMutableAudioMixInputParameters

<sub>Class</sub>

The parameters you use when adding an audio track to a mix.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVMutableAudioMixInputParameters
```

## Relationships

- **Inherits From**: [AVAudioMixInputParameters](avaudiomixinputparameters.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating input parameters

- [+ audioMixInputParametersWithTrack:](<avmutableaudiomixinputparameters/init(track_).md>) — Creates a mutable input parameters object for a given track.

### Managing the track ID

- [trackID](avmutableaudiomixinputparameters/trackid.md) — The identifier of the audio track to which the parameters should be applied.

### Setting the volume

- [- setVolume:atTime:](<avmutableaudiomixinputparameters/setvolume(__at_).md>) — Sets the value of the audio volume starting at the specified time.
- [- setVolumeRampFromStartVolume:toEndVolume:timeRange:](<avmutableaudiomixinputparameters/setvolumeramp(fromstartvolume_toendvolume_timerange_).md>) — Sets a volume ramp to apply during a specified time range.

### Getting an audio tap

- [audioTapProcessor](avmutableaudiomixinputparameters/audiotapprocessor.md) — The audio processing tap associated with the track.

### Time pitch settings

- [audioTimePitchAlgorithm](avmutableaudiomixinputparameters/audiotimepitchalgorithm.md) — The processing algorithm used to manage audio pitch for scaled audio edits.
- [AVAudioTimePitchAlgorithm](avaudiotimepitchalgorithm.md) — An algorithm used to set the audio pitch as the rate changes.

## See Also

### Mixing

- [AVAudioMix](avaudiomix.md) — An object that manages the input parameters for mixing audio tracks.
- [AVAudioMixInputParameters](avaudiomixinputparameters.md) — An object that represents the parameters that you apply when adding an audio track to a mix.
- [AVAudioMixInputParametersTrackID](avaudiomixinputparameterstrackid.md) — Special value for the trackID property of AVAudioMixInputParameters. _(beta)_
- [AVMutableAudioMix](avmutableaudiomix.md) — An object that manages the input parameters for mixing audio tracks.
