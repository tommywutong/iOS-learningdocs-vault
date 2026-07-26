---
title: rate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/rate
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/rate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/rate.json'
content_hash: 'sha256:0ffc5723d3913d8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# rate

<sub>Instance Property</sub>

The current playback rate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var rate: Float { get set }
```

## See Also

### Controlling playback

- [defaultRate](defaultrate.md) — A default rate at which to begin playback.
- [- play](<play().md>) — Begins playback of the current item.
- [- pause](<pause().md>) — Pauses playback of the current item.
- [AVPlayerRateDidChangeNotification](ratedidchangenotification.md) — A notification that a player posts when its rate changes.
- [AVPlayerRateDidChangeReasonPlayheadReachedLiveEdge](ratedidchangereason/playheadreachedliveedge.md) — Indicates that the player automatically switched the playback rate from \> 1.0 back to 1.0 when the playhead reached the live edge during live streaming.
- [AVPlayerRateDidChangeReasonReversePlaybackReachedStartOfSeekableRange](ratedidchangereason/reverseplaybackreachedstartofseekablerange.md) — Indicates that the player automatically switched rate to 1.0 when the reverse playback reached start of seekable range. only for live.
