---
title: AVPlayer.HDRMode
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 11.2+（26.0 起废弃）, iPadOS 11.2+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, tvOS 11.2+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avplayer/hdrmode
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/hdrmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/hdrmode.json'
content_hash: 'sha256:ca592ff776a56624'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# AVPlayer.HDRMode

<sub>Structure</sub>

A bitfield type that specifies an HDR mode.

> [!warning] Deprecated
> The deprecated availableHDRModes uses this enum. Use eligibleForHDRPlayback instead

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct HDRMode
```

## Overview

These modes define the available HDR modes. Query [availableHDRModes](availablehdrmodes.md) to find the HDR modes available for a device.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### HDR modes

- [AVPlayerHDRModeHLG](hdrmode/hlg.md) — The Hybrid Log-Gamma HDR mode is available. _(deprecated)_
- [AVPlayerHDRModeHDR10](hdrmode/hdr10.md) — The HDR10 HDR mode is available. _(deprecated)_
- [AVPlayerHDRModeDolbyVision](hdrmode/dolbyvision.md) — The Dolby Vision HDR mode is available. _(deprecated)_

### Initializers

- [init(rawValue:)](<hdrmode/init(rawvalue_).md>) — Creates an HDR mode with a string value. _(deprecated)_

## See Also

### Determining HDR playback eligibility

- [eligibleForHDRPlayback](eligibleforhdrplayback.md) — A Boolean value that indicates whether the current device can present content to an HDR display.
- [availableHDRModes](availablehdrmodes.md) — The HDR modes that are available for playback. _(deprecated)_
- [AVPlayerEligibleForHDRPlaybackDidChangeNotification](eligibleforhdrplaybackdidchangenotification.md) — A notification that’s posted whenever HDR playback eligibility changes.
