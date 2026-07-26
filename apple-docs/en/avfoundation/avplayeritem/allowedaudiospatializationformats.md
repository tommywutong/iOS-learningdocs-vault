---
title: allowedAudioSpatializationFormats
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/allowedaudiospatializationformats
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/allowedaudiospatializationformats'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/allowedaudiospatializationformats.json'
content_hash: 'sha256:3253f7a1988fd4c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# allowedAudioSpatializationFormats

<sub>Instance Property</sub>

The source audio channel layouts the player item supports for spatialization.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated var allowedAudioSpatializationFormats: AVAudioSpatializationFormats { get set }
```

## Discussion

Spatialization uses psychoacoustic methods to create a more immersive audio experience when playing content on specialized headphones and speaker arrangements.

The default value for video content is [AVAudioSpatializationFormatMonoStereoAndMultichannel](../avaudiospatializationformats/monostereoandmultichannel.md), and [AVAudioSpatializationFormatMultichannel](../avaudiospatializationformats/multichannel.md) for audio-only content. Your app can set a preferred spatialization format, but a user can change the audio spatialization behavior in Control Center.

This property isn’t key-value observable.

> [!important] Important
> It’s incorrect to render binaural recordings with spatialization. Content tagged with a binaural channel layout ignores this property value.

## See Also

### Configuring audio behavior

- [volume](../avplayer/volume.md) — The audio playback volume for the player.
- [muted](../avplayer/ismuted.md) — A Boolean value that indicates whether the audio output of the player is muted.
- [audioSpatializationAllowed](isaudiospatializationallowed.md) — A Boolean value that indicates whether the player item allows spatialized audio playback. _(deprecated)_
- [audioOutputSuppressedDueToNonMixableAudioRoute](../avplayer/audiooutputsuppressedduetononmixableaudioroute.md) — Whether the player’s audio output is suppressed due to being on a non-mixable audio route.
- [intendedSpatialAudioExperience](../avplayer/intendedspatialaudioexperience-1bd87.md) — The player’s intended Spatial Audio experience.
