---
title: eligibleForHDRPlaybackDidChangeNotification
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, macOS 10.15+, tvOS 13.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/eligibleforhdrplaybackdidchangenotification
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/eligibleforhdrplaybackdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/eligibleforhdrplaybackdidchangenotification.json'
content_hash: 'sha256:0eb62853de660c93'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# eligibleForHDRPlaybackDidChangeNotification

<sub>Type Property</sub>

A notification that’s posted whenever HDR playback eligibility changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class let eligibleForHDRPlaybackDidChangeNotification: NSNotification.Name
```

## Discussion

The system may post this notification if a user connects or disconnects a display, or makes other system resource changes.

## See Also

### Determining HDR playback eligibility

- [eligibleForHDRPlayback](eligibleforhdrplayback.md) — A Boolean value that indicates whether the current device can present content to an HDR display.
- [availableHDRModes](availablehdrmodes.md) — The HDR modes that are available for playback. _(deprecated)_
- [HDRMode](hdrmode.md) — A bitfield type that specifies an HDR mode. _(deprecated)_
