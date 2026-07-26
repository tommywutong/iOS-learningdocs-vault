---
title: audioTimePitchAlgorithm
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/audiotimepitchalgorithm
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/audiotimepitchalgorithm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/audiotimepitchalgorithm.json'
content_hash: 'sha256:4d404abd9f58b8ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# audioTimePitchAlgorithm

<sub>Instance Property</sub>

The processing algorithm used to manage audio pitch for scaled audio edits.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var audioTimePitchAlgorithm: AVAudioTimePitchAlgorithm { get set }
```

## Discussion

The supported constants are defined in Time Pitch Algorithm Settings.

An [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) will be raised if this property is set to a value other than the defined constants.

## See Also

### Configuring audio

- [audioMix](audiomix.md) — The audio mix parameters to be applied during playback.
- [allowedAudioSpatializationFormats](allowedaudiospatializationformats.md) — The source audio channel layouts the player item supports for spatialization.
- [AVAudioSpatializationFormats](../avaudiospatializationformats.md) — A structure that defines the spatialization formats that a player item supports.
- [audioSpatializationAllowed](isaudiospatializationallowed.md) — A Boolean value that indicates whether the player item allows spatialized audio playback. _(deprecated)_
