---
title: AVPlayerAvailableHDRModesDidChangeNotification
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 11.2+（26.0 起废弃）, iPadOS 11.2+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, tvOS 11.2+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeravailablehdrmodesdidchangenotification
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeravailablehdrmodesdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeravailablehdrmodesdidchangenotification.json'
content_hash: 'sha256:768e804215e77e07'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerAvailableHDRModesDidChangeNotification

<sub>Global Variable</sub>

A notification that fires whenever availableHDRModes changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern NSNotificationName const AVPlayerAvailableHDRModesDidChangeNotification;
```

## Discussion

This notification fires when a value is added or removed from the list of availableHDRModes. This can be caused by display connection/disconnection or resource changes.

## See Also

### Determining HDR playback eligibility

- [eligibleForHDRPlayback](avplayer/eligibleforhdrplayback.md) — A Boolean value that indicates whether the current device can present content to an HDR display.
- [availableHDRModes](avplayer/availablehdrmodes.md) — The HDR modes that are available for playback. _(deprecated)_
- [HDRMode](avplayer/hdrmode.md) — A bitfield type that specifies an HDR mode. _(deprecated)_
- [AVPlayerEligibleForHDRPlaybackDidChangeNotification](avplayer/eligibleforhdrplaybackdidchangenotification.md) — A notification that’s posted whenever HDR playback eligibility changes.
