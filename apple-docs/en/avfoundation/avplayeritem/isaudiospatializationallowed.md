---
title: isAudioSpatializationAllowed
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+（18.0 起废弃）, iPadOS 13.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.15+（15.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avplayeritem/isaudiospatializationallowed
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/isaudiospatializationallowed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/isaudiospatializationallowed.json'
content_hash: 'sha256:3c19b562a90f002e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# isAudioSpatializationAllowed

<sub>Instance Property</sub>

A Boolean value that indicates whether the player item allows spatialized audio playback.

> [!warning] Deprecated
> Use [allowedAudioSpatializationFormats](allowedaudiospatializationformats.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var isAudioSpatializationAllowed: Bool { get set }
```

## See Also

### Configuring audio behavior

- [volume](../avplayer/volume.md) — The audio playback volume for the player.
- [muted](../avplayer/ismuted.md) — A Boolean value that indicates whether the audio output of the player is muted.
- [allowedAudioSpatializationFormats](allowedaudiospatializationformats.md) — The source audio channel layouts the player item supports for spatialization.
- [audioOutputSuppressedDueToNonMixableAudioRoute](../avplayer/audiooutputsuppressedduetononmixableaudioroute.md) — Whether the player’s audio output is suppressed due to being on a non-mixable audio route.
- [intendedSpatialAudioExperience](../avplayer/intendedspatialaudioexperience-1bd87.md) — The player’s intended Spatial Audio experience.
