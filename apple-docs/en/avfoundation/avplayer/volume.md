---
title: volume
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/volume
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/volume'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/volume.json'
content_hash: 'sha256:baaf31ad1e2d331e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# volume

<sub>Instance Property</sub>

The audio playback volume for the player.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var volume: Float { get set }
```

## Discussion

A value of `0.0` indicates silence; a value of `1.0` (the default) indicates full audio volume for the player instance.

This property is used to control the player audio volume relative to the system volume. There is no programmatic way to control the system volume in iOS, but you can use the MediaPlayer framework’s [MPVolumeView](../../mediaplayer/mpvolumeview.md) class to present a standard user interface for controlling system volume.

## See Also

### Configuring audio behavior

- [muted](ismuted.md) — A Boolean value that indicates whether the audio output of the player is muted.
- [allowedAudioSpatializationFormats](../avplayeritem/allowedaudiospatializationformats.md) — The source audio channel layouts the player item supports for spatialization.
- [audioSpatializationAllowed](../avplayeritem/isaudiospatializationallowed.md) — A Boolean value that indicates whether the player item allows spatialized audio playback. _(deprecated)_
- [audioOutputSuppressedDueToNonMixableAudioRoute](audiooutputsuppressedduetononmixableaudioroute.md) — Whether the player’s audio output is suppressed due to being on a non-mixable audio route.
- [intendedSpatialAudioExperience](intendedspatialaudioexperience-1bd87.md) — The player’s intended Spatial Audio experience.
