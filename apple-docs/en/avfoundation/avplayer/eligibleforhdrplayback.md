---
title: eligibleForHDRPlayback
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, macOS 10.15+, tvOS 13.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/eligibleforhdrplayback
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/eligibleforhdrplayback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/eligibleforhdrplayback.json'
content_hash: 'sha256:e3e59acf94406b13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# eligibleForHDRPlayback

<sub>Type Property</sub>

A Boolean value that indicates whether the current device can present content to an HDR display.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated class var eligibleForHDRPlayback: Bool { get }
```

## Discussion

This property is not key-value observable.

## See Also

### Determining HDR playback eligibility

- [availableHDRModes](availablehdrmodes.md) — The HDR modes that are available for playback. _(deprecated)_
- [HDRMode](hdrmode.md) — A bitfield type that specifies an HDR mode. _(deprecated)_
- [AVPlayerEligibleForHDRPlaybackDidChangeNotification](eligibleforhdrplaybackdidchangenotification.md) — A notification that’s posted whenever HDR playback eligibility changes.
