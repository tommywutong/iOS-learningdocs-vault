---
title: audioOutputSuppressedDueToNonMixableAudioRoute
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/audiooutputsuppressedduetononmixableaudioroute
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/audiooutputsuppressedduetononmixableaudioroute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/audiooutputsuppressedduetononmixableaudioroute.json'
content_hash: 'sha256:87834c05247c4f83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# audioOutputSuppressedDueToNonMixableAudioRoute

<sub>Instance Property</sub>

Whether the player’s audio output is suppressed due to being on a non-mixable audio route.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var audioOutputSuppressedDueToNonMixableAudioRoute: Bool { get }
```

## Discussion

If YES, the player’s audio output is suppressed. The player is muted while on a non-mixable audio route and cannot play audio. The player’s mute property does not reflect the true mute status. If NO, the player’s audio output is not suppressed. The player may be muted or unmuted while on a non-mixable audio route and can play audio. The player’s mute property reflects the true mute status. In a non-mixable audio route, only one player can play audio. To play audio in non-mixable states, the player must be specified as the priority participant in AVRoutingPlaybackArbiter.preferredParticipantForNonMixableAudioRoutes. If this player becomes the preferred player, it will gain audio priority and suppress the audio of all other players. If another participant becomes the preferred participant, this player will lose audio priority and have their audio suppressed. This property is key-value observed.

## See Also

### Configuring audio behavior

- [volume](volume.md) — The audio playback volume for the player.
- [muted](ismuted.md) — A Boolean value that indicates whether the audio output of the player is muted.
- [allowedAudioSpatializationFormats](../avplayeritem/allowedaudiospatializationformats.md) — The source audio channel layouts the player item supports for spatialization.
- [audioSpatializationAllowed](../avplayeritem/isaudiospatializationallowed.md) — A Boolean value that indicates whether the player item allows spatialized audio playback. _(deprecated)_
- [intendedSpatialAudioExperience](intendedspatialaudioexperience-1bd87.md) — The player’s intended Spatial Audio experience.
