---
title: audioMix
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/audiomix
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/audiomix'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/audiomix.json'
content_hash: 'sha256:1ae8becc30bf99a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# audioMix

<sub>Instance Property</sub>

The audio mix parameters to be applied during playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var audioMix: AVAudioMix? { get set }
```

## Discussion

An audio mix can only be used with file-based media and is not supported for use with media served using HTTP Live Streaming.

## See Also

### Configuring audio

- [audioTimePitchAlgorithm](audiotimepitchalgorithm.md) — The processing algorithm used to manage audio pitch for scaled audio edits.
- [allowedAudioSpatializationFormats](allowedaudiospatializationformats.md) — The source audio channel layouts the player item supports for spatialization.
- [AVAudioSpatializationFormats](../avaudiospatializationformats.md) — A structure that defines the spatialization formats that a player item supports.
- [audioSpatializationAllowed](isaudiospatializationallowed.md) — A Boolean value that indicates whether the player item allows spatialized audio playback. _(deprecated)_
