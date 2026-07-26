---
title: dolbyVision
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.2+（26.0 起废弃）, iPadOS 11.2+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, tvOS 11.2+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avplayer/hdrmode/dolbyvision
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/hdrmode/dolbyvision'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/hdrmode/dolbyvision.json'
content_hash: 'sha256:406463e54b1dff82'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVPlayer](../../avplayer.md) · [HDRMode](../hdrmode.md)

# dolbyVision

<sub>Type Property</sub>

The Dolby Vision HDR mode is available.

> [!warning] Deprecated
> The deprecated availableHDRModes uses this enum. Use eligibleForHDRPlayback instead

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var dolbyVision: AVPlayer.HDRMode { get }
```

## See Also

### HDR modes

- [AVPlayerHDRModeHLG](hlg.md) — The Hybrid Log-Gamma HDR mode is available. _(deprecated)_
- [AVPlayerHDRModeHDR10](hdr10.md) — The HDR10 HDR mode is available. _(deprecated)_
