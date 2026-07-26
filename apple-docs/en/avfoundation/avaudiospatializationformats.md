---
title: AVAudioSpatializationFormats
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avaudiospatializationformats
source_url: 'https://developer.apple.com/documentation/avfoundation/avaudiospatializationformats'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avaudiospatializationformats.json'
content_hash: 'sha256:938f81b4ffb7826f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAudioSpatializationFormats

<sub>Structure</sub>

A structure that defines the spatialization formats that a player item supports.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AVAudioSpatializationFormats
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Spatialization formats

- [AVAudioSpatializationFormatMonoAndStereo](avaudiospatializationformats/monoandstereo.md) — A value that indicates the player item only supports mono and stereo layouts for audio spatialization.
- [AVAudioSpatializationFormatMultichannel](avaudiospatializationformats/multichannel.md) — A value that indicates the player item only supports multichannel layouts for audio spatialization.
- [AVAudioSpatializationFormatMonoStereoAndMultichannel](avaudiospatializationformats/monostereoandmultichannel.md) — A value that indicates the player item supports mono, stereo, and multichannel layouts for audio spatialization.

### Initializers

- [init(rawValue:)](<avaudiospatializationformats/init(rawvalue_).md>) — Initializes a format with a string value.

## See Also

### Configuring audio

- [audioMix](avplayeritem/audiomix.md) — The audio mix parameters to be applied during playback.
- [audioTimePitchAlgorithm](avplayeritem/audiotimepitchalgorithm.md) — The processing algorithm used to manage audio pitch for scaled audio edits.
- [allowedAudioSpatializationFormats](avplayeritem/allowedaudiospatializationformats.md) — The source audio channel layouts the player item supports for spatialization.
- [audioSpatializationAllowed](avplayeritem/isaudiospatializationallowed.md) — A Boolean value that indicates whether the player item allows spatialized audio playback. _(deprecated)_
