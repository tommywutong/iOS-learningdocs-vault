---
title: reversePlaybackReachedStartOfSeekableRange
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, tvOS 26.4+, visionOS 26.4+, watchOS 26.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/ratedidchangereason/reverseplaybackreachedstartofseekablerange
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/ratedidchangereason/reverseplaybackreachedstartofseekablerange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/ratedidchangereason/reverseplaybackreachedstartofseekablerange.json'
content_hash: 'sha256:22ab97976f5af928'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVPlayer](../../avplayer.md) · [RateDidChangeReason](../ratedidchangereason.md)

# reversePlaybackReachedStartOfSeekableRange

<sub>Type Property</sub>

Indicates that the player automatically switched rate to 1.0 when the reverse playback reached start of seekable range. only for live.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let reversePlaybackReachedStartOfSeekableRange: AVPlayer.RateDidChangeReason
```

## See Also

### Controlling playback

- [defaultRate](../defaultrate.md) — A default rate at which to begin playback.
- [- play](<../play().md>) — Begins playback of the current item.
- [- pause](<../pause().md>) — Pauses playback of the current item.
- [rate](../rate.md) — The current playback rate.
- [AVPlayerRateDidChangeNotification](../ratedidchangenotification.md) — A notification that a player posts when its rate changes.
- [AVPlayerRateDidChangeReasonPlayheadReachedLiveEdge](playheadreachedliveedge.md) — Indicates that the player automatically switched the playback rate from \> 1.0 back to 1.0 when the playhead reached the live edge during live streaming.
