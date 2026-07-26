---
title: isPlaybackBufferFull
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/isplaybackbufferfull
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/isplaybackbufferfull'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/isplaybackbufferfull.json'
content_hash: 'sha256:4f92fe5139fb7389'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# isPlaybackBufferFull

<sub>Instance Property</sub>

A Boolean value that indicates whether the internal media buffer is full and that further I/O is suspended.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var isPlaybackBufferFull: Bool { get }
```

## Discussion

Despite the playback buffer reaching capacity there might not exist sufficient statistical data to support a [playbackLikelyToKeepUp](isplaybacklikelytokeepup.md) prediction of [true](../../swift/true.md).

## See Also

### Determining buffering status

- [playbackLikelyToKeepUp](isplaybacklikelytokeepup.md) — A Boolean value that indicates whether the item will likely play through without stalling.
- [playbackBufferEmpty](isplaybackbufferempty.md) — A Boolean value that indicates whether playback has consumed all buffered media and that playback will stall or end.
