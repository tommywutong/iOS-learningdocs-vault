---
title: intendedSpatialAudioExperience
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/intendedspatialaudioexperience-3uy8g
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/intendedspatialaudioexperience-3uy8g'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/intendedspatialaudioexperience-3uy8g.json'
content_hash: 'sha256:5f001cb2c685b5c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# intendedSpatialAudioExperience

<sub>Instance Property</sub>

The AVPlayer’s intended spatial audio experience.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy) CASpatialAudioExperience * intendedSpatialAudioExperience;
```

## Discussion

The default value of CAAutomaticSpatialAudio means the player uses its AVAudioSession’s intended spatial experience. If the anchoring strategy is impossible (e.g. it uses a destroyed UIScene’s identifier), the player follows a “front” anchoring strategy instead.

## See Also

### Configuring audio behavior

- [volume](volume.md) — The audio playback volume for the player.
- [muted](ismuted.md) — A Boolean value that indicates whether the audio output of the player is muted.
- [allowedAudioSpatializationFormats](../avplayeritem/allowedaudiospatializationformats.md) — The source audio channel layouts the player item supports for spatialization.
- [audioSpatializationAllowed](../avplayeritem/isaudiospatializationallowed.md) — A Boolean value that indicates whether the player item allows spatialized audio playback. _(deprecated)_
- [audioOutputSuppressedDueToNonMixableAudioRoute](audiooutputsuppressedduetononmixableaudioroute.md) — Whether the player’s audio output is suppressed due to being on a non-mixable audio route.
