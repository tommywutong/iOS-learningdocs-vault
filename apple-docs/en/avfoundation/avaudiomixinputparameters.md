---
title: AVAudioMixInputParameters
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avaudiomixinputparameters
source_url: 'https://developer.apple.com/documentation/avfoundation/avaudiomixinputparameters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avaudiomixinputparameters.json'
content_hash: 'sha256:3ce25346795b66fb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAudioMixInputParameters

<sub>Class</sub>

An object that represents the parameters that you apply when adding an audio track to a mix.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVAudioMixInputParameters
```

## Overview

You use an instance `AVAudioMixInputParameters` to apply audio volume ramps for an input to an audio mix. Mix parameters are associated with audio tracks via the [trackID](avaudiomixinputparameters/trackid.md) property.

Audio volume is currently supported as a time-varying parameter. `AVAudioMixInputParameters` has a mutable subclass, [AVMutableAudioMixInputParameters](avmutableaudiomixinputparameters.md).

Before the first time at which a volume is set, a volume of 1.0 used; after the last time for which a volume has been set, the last volume is used. Within the time range of a volume ramp, the volume is interpolated between the start volume and end volume of the ramp. For example, setting the volume to 1.0 at time 0 and also setting a volume ramp from a volume of 0.5 to 0.2 with a timeRange of [4.0, 5.0] results in an audio volume parameters that hold the volume constant at 1.0 from 0.0 sec to 4.0 sec, then cause it to jump to 0.5 and descend to 0.2 from 4.0 sec to 9.0 sec, holding constant at 0.2 thereafter.

Given that this is an immutable variant of the object, you should not allocate and initialize a version of this class yourself. Other classes may return instances of this class.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVMutableAudioMixInputParameters](avmutableaudiomixinputparameters.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting the track ID

- [trackID](avaudiomixinputparameters/trackid.md) — The identifier of the audio track to which the parameters should be applied.

### Getting volume ramps

- [- getVolumeRampForTime:startVolume:endVolume:timeRange:](<avaudiomixinputparameters/getvolumeramp(for_startvolume_endvolume_timerange_).md>) — Retrieves the volume ramp that includes the specified time.

### Getting an audio tap

- [audioTapProcessor](avaudiomixinputparameters/audiotapprocessor.md) — The audio processing tap associated with the track.

### Getting the time pitch algorithm setting

- [audioTimePitchAlgorithm](avaudiomixinputparameters/audiotimepitchalgorithm.md) — The processing algorithm used to manage audio pitch for scaled audio edits.
- [AVAudioTimePitchAlgorithm](avaudiotimepitchalgorithm.md) — An algorithm used to set the audio pitch as the rate changes.

## See Also

### Mixing

- [AVAudioMix](avaudiomix.md) — An object that manages the input parameters for mixing audio tracks.
- [AVAudioMixInputParametersTrackID](avaudiomixinputparameterstrackid.md) — Special value for the trackID property of AVAudioMixInputParameters. _(beta)_
- [AVMutableAudioMix](avmutableaudiomix.md) — An object that manages the input parameters for mixing audio tracks.
- [AVMutableAudioMixInputParameters](avmutableaudiomixinputparameters.md) — The parameters you use when adding an audio track to a mix.
