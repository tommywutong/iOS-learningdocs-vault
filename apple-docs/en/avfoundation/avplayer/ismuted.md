---
title: isMuted
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/ismuted
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/ismuted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/ismuted.json'
content_hash: 'sha256:6002d321e9cd4636'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# isMuted

<sub>Instance Property</sub>

A Boolean value that indicates whether the audio output of the player is muted.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var isMuted: Bool { get set }
```

## See Also

### Configuring audio behavior

- [volume](volume.md) — The audio playback volume for the player.
- [allowedAudioSpatializationFormats](../avplayeritem/allowedaudiospatializationformats.md) — The source audio channel layouts the player item supports for spatialization.
- [audioSpatializationAllowed](../avplayeritem/isaudiospatializationallowed.md) — A Boolean value that indicates whether the player item allows spatialized audio playback. _(deprecated)_
- [audioOutputSuppressedDueToNonMixableAudioRoute](audiooutputsuppressedduetononmixableaudioroute.md) — Whether the player’s audio output is suppressed due to being on a non-mixable audio route.
- [intendedSpatialAudioExperience](intendedspatialaudioexperience-1bd87.md) — The player’s intended Spatial Audio experience.
