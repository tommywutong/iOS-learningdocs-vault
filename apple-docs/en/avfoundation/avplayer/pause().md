---
title: pause()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/pause()
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/pause()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/pause%28%29.json'
content_hash: 'sha256:752559769a7ee001'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# pause()

<sub>Instance Method</sub>

Pauses playback of the current item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func pause()
```

## Discussion

Calling this method is the same as setting the [rate](rate.md) to `0.0`.

## See Also

### Controlling playback

- [defaultRate](defaultrate.md) — A default rate at which to begin playback.
- [- play](<play().md>) — Begins playback of the current item.
- [rate](rate.md) — The current playback rate.
- [AVPlayerRateDidChangeNotification](ratedidchangenotification.md) — A notification that a player posts when its rate changes.
- [AVPlayerRateDidChangeReasonPlayheadReachedLiveEdge](ratedidchangereason/playheadreachedliveedge.md) — Indicates that the player automatically switched the playback rate from \> 1.0 back to 1.0 when the playhead reached the live edge during live streaming.
- [AVPlayerRateDidChangeReasonReversePlaybackReachedStartOfSeekableRange](ratedidchangereason/reverseplaybackreachedstartofseekablerange.md) — Indicates that the player automatically switched rate to 1.0 when the reverse playback reached start of seekable range. only for live.
