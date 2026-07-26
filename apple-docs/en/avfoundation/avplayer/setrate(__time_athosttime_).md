---
title: 'setRate(_:time:atHostTime:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayer/setrate(_:time:athosttime:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/setrate(_:time:athosttime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/setrate%28_%3Atime%3Aathosttime%3A%29.json'
content_hash: 'sha256:445a55206c4f24ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# setRate(_:time:atHostTime:)

<sub>Instance Method</sub>

Synchronizes the playback rate and time of the current item with an external source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func setRate(_ rate: Float, time itemTime: CMTime, atHostTime hostClockTime: CMTime)
```

## Parameters

- `rate` — The playback rate for the item.

- `itemTime` — The precise time at which to match playback of the item. To use the current item’s current time, specify [invalid](../../coremedia/cmtime/invalid.md).

- `hostClockTime` — The host time at which to synchronize playback. If you specify [invalid](../../coremedia/cmtime/invalid.md), the rate and time are set together without any external synchronization.

## Discussion

This method adjusts the current item’s timebase so that the time in `itemTime` is in sync with the time in `hostClockTime`. Thus, if `hostClockTime` specifies a time in the past, the item’s timebase is adjusted to make it appear as if the item has been running at the specified rate since `itemTime`. And if `hostClockTime` specifies a time in the future, playback is adjusted backward (if possible) so that the value in `itemTime` occurs at the precise moment the host’s clock reaches the value in `hostClockTime`. If there is no content to play before the time specified by `itemTime`, playback holds until the two times come into sync.

This method does not ensure that media data is loaded before the timebase starts moving. However, if you specify a host time in the near future, that would give you some time to load the media data and prepare for playback.

> [!important] Important
> The value of [automaticallyWaitsToMinimizeStalling](automaticallywaitstominimizestalling.md) must be set to `false` before calling this method. If the property value is `true`, calling this method results in the system raising an invalid argument exception.

## See Also

### Synchronizing multiple players

- [- prerollAtRate:completionHandler:](<preroll(atrate_completionhandler_).md>) — Begins loading media data to prime the media pipelines for playback.
- [- cancelPendingPrerolls](<cancelpendingprerolls().md>) — Cancels any pending preroll requests and invokes the corresponding completion handlers, if present.
- [sourceClock](sourceclock.md) — A clock the player uses for item time bases.
- [masterClock](masterclock.md) — The host clock for item time bases. _(deprecated)_
