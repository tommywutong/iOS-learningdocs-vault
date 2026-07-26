---
title: intendedSpatialAudioExperience
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/intendedspatialaudioexperience-1bd87
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/intendedspatialaudioexperience-1bd87'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/intendedspatialaudioexperience-1bd87.json'
content_hash: 'sha256:2b50085f8054040a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# intendedSpatialAudioExperience

<sub>Instance Property</sub>

The player’s intended Spatial Audio experience.

<sub>visionOS</sub>

```swift
nonisolated var intendedSpatialAudioExperience: any SpatialAudioExperience { get set }
```

## Discussion

If unspecified, the property value defaults to [CAAutomaticSpatialAudio](../../audiotoolbox/caautomaticspatialaudio.md).

## See Also

### Configuring audio behavior

- [volume](volume.md) — The audio playback volume for the player.
- [muted](ismuted.md) — A Boolean value that indicates whether the audio output of the player is muted.
- [allowedAudioSpatializationFormats](../avplayeritem/allowedaudiospatializationformats.md) — The source audio channel layouts the player item supports for spatialization.
- [audioSpatializationAllowed](../avplayeritem/isaudiospatializationallowed.md) — A Boolean value that indicates whether the player item allows spatialized audio playback. _(deprecated)_
- [audioOutputSuppressedDueToNonMixableAudioRoute](audiooutputsuppressedduetononmixableaudioroute.md) — Whether the player’s audio output is suppressed due to being on a non-mixable audio route.
