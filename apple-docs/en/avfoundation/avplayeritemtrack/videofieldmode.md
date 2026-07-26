---
title: videoFieldMode
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemtrack/videofieldmode
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemtrack/videofieldmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemtrack/videofieldmode.json'
content_hash: 'sha256:e9a920be2ddb5926'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemTrack](../avplayeritemtrack.md)

# videoFieldMode

<sub>Instance Property</sub>

A mode that specifies the handling of video frames that contain multiple fields.

<sub>macOS</sub>

```swift
nonisolated var videoFieldMode: String? { get set }
```

## Discussion

A value of `nil` indicates default processing of video frames. To deinterlace video fields, set this property value to [AVPlayerItemTrackVideoFieldModeDeinterlaceFields](../avplayeritemtrackvideofieldmodedeinterlacefields.md).

## See Also

### Configuring video properties

- [currentVideoFrameRate](currentvideoframerate.md) — The current frame rate of the video track as it plays.
- [AVPlayerItemTrackVideoFieldModeDeinterlaceFields](../avplayeritemtrackvideofieldmodedeinterlacefields.md) — A video field mode that requests deinterlacing of video fields.
