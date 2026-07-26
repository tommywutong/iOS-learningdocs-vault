---
title: availableHDRModes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.2+（26.0 起废弃）, iPadOS 11.2+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, tvOS 11.2+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avplayer/availablehdrmodes
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/availablehdrmodes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/availablehdrmodes.json'
content_hash: 'sha256:bdbbd15233709945'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# availableHDRModes

<sub>Type Property</sub>

The HDR modes that are available for playback.

> [!warning] Deprecated
> Use eligibleForHDRPlayback instead

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated class var availableHDRModes: AVPlayer.HDRMode { get }
```

## Discussion

This property indicates all of the HDR modes that the device can play. A value of `0` indicates the device doesn’t support HDR. Each value indicates that an appropriate HDR display is available for the specified HDR mode. Additionally, the device must be capable of playing the specified HDR type.

This property doesn’t indicate whether a video contains HDR content, HDR video is currently playing, or if video is playing on an HDR display.

> [!important] Important
> Mac apps built with Mac Catalyst don’t support HDR playback on Intel-based Mac computers. When playing HDR content over HTTP Live Streaming, [AVPlayer](../avplayer.md) selects the SDR variant playlist. When playing file-based media, HDR content is tone mapped to SDR before it’s rendered onscreen.

## See Also

### Determining HDR playback eligibility

- [eligibleForHDRPlayback](eligibleforhdrplayback.md) — A Boolean value that indicates whether the current device can present content to an HDR display.
- [HDRMode](hdrmode.md) — A bitfield type that specifies an HDR mode. _(deprecated)_
- [AVPlayerEligibleForHDRPlaybackDidChangeNotification](eligibleforhdrplaybackdidchangenotification.md) — A notification that’s posted whenever HDR playback eligibility changes.
