---
title: isPlaybackBufferEmpty
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/isplaybackbufferempty
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/isplaybackbufferempty'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/isplaybackbufferempty.json'
content_hash: 'sha256:ecf26659114ad6de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# isPlaybackBufferEmpty

<sub>Instance Property</sub>

A Boolean value that indicates whether playback has consumed all buffered media and that playback will stall or end.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var isPlaybackBufferEmpty: Bool { get }
```

## See Also

### Determining buffering status

- [playbackLikelyToKeepUp](isplaybacklikelytokeepup.md) — A Boolean value that indicates whether the item will likely play through without stalling.
- [playbackBufferFull](isplaybackbufferfull.md) — A Boolean value that indicates whether the internal media buffer is full and that further I/O is suspended.
