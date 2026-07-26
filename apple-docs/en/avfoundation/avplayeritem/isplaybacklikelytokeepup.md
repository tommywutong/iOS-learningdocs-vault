---
title: isPlaybackLikelyToKeepUp
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/isplaybacklikelytokeepup
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/isplaybacklikelytokeepup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/isplaybacklikelytokeepup.json'
content_hash: 'sha256:9ef61f7b0380fa39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# isPlaybackLikelyToKeepUp

<sub>Instance Property</sub>

A Boolean value that indicates whether the item will likely play through without stalling.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var isPlaybackLikelyToKeepUp: Bool { get }
```

## Discussion

This property communicates a prediction of playability. Factors considered in this prediction include I/O throughput and media decode performance. It is possible for `playbackLikelyToKeepUp` to indicate [false](../../swift/false.md) while the property [playbackBufferFull](isplaybackbufferfull.md) indicates [true](../../swift/true.md). In this event the playback buffer has reached capacity but there isn’t the statistical data to support a prediction that playback is likely to keep up in the future. It is up to you to decide whether to continue media playback.

## See Also

### Determining buffering status

- [playbackBufferFull](isplaybackbufferfull.md) — A Boolean value that indicates whether the internal media buffer is full and that further I/O is suspended.
- [playbackBufferEmpty](isplaybackbufferempty.md) — A Boolean value that indicates whether playback has consumed all buffered media and that playback will stall or end.
