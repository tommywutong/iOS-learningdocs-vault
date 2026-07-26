---
title: currentVideoFrameRate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemtrack/currentvideoframerate
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemtrack/currentvideoframerate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemtrack/currentvideoframerate.json'
content_hash: 'sha256:50b963f5c3c181d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemTrack](../avplayeritemtrack.md)

# currentVideoFrameRate

<sub>Instance Property</sub>

The current frame rate of the video track as it plays.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated var currentVideoFrameRate: Float { get }
```

## Discussion

If the media type of the [assetTrack](assettrack.md) is [AVMediaTypeVideo](../avmediatype/video.md), the property indicates the current frame rate of the track as it plays, in frames per second. If the item isn’t playing, or if the media type of the track isn’t video, the value of this property is `0.0`.

This property isn’t key-value observable.

## See Also

### Configuring video properties

- [videoFieldMode](videofieldmode.md) — A mode that specifies the handling of video frames that contain multiple fields.
- [AVPlayerItemTrackVideoFieldModeDeinterlaceFields](../avplayeritemtrackvideofieldmodedeinterlacefields.md) — A video field mode that requests deinterlacing of video fields.
