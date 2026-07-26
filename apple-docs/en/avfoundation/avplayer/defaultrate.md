---
title: defaultRate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/defaultrate
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/defaultrate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/defaultrate.json'
content_hash: 'sha256:442bcf3b2dfb0c2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# defaultRate

<sub>Instance Property</sub>

A default rate at which to begin playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var defaultRate: Float { get set }
```

## Discussion

This value represents the default playback rate the player uses when you call its [- play](<play().md>) method. After playback begins, the rate may differ from the default if you modify the player’s [rate](rate.md) value, such as by calling [- pause](<pause().md>).

> [!important] Important
> Begin playback by calling the [- play](<play().md>) method. Don’t start playback by setting the [rate](rate.md) property value to `1.0`. Instead, use [rate](rate.md) to make immediate, temporary changes to the playback rate. The next time you call the [- play](<play().md>) method, the player restores the rate to the value of [defaultRate](defaultrate.md).

## See Also

### Controlling playback

- [- play](<play().md>) — Begins playback of the current item.
- [- pause](<pause().md>) — Pauses playback of the current item.
- [rate](rate.md) — The current playback rate.
- [AVPlayerRateDidChangeNotification](ratedidchangenotification.md) — A notification that a player posts when its rate changes.
- [AVPlayerRateDidChangeReasonPlayheadReachedLiveEdge](ratedidchangereason/playheadreachedliveedge.md) — Indicates that the player automatically switched the playback rate from \> 1.0 back to 1.0 when the playhead reached the live edge during live streaming.
- [AVPlayerRateDidChangeReasonReversePlaybackReachedStartOfSeekableRange](ratedidchangereason/reverseplaybackreachedstartofseekablerange.md) — Indicates that the player automatically switched rate to 1.0 when the reverse playback reached start of seekable range. only for live.
