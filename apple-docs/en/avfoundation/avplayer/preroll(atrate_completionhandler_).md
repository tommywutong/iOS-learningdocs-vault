---
title: 'preroll(atRate:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayer/preroll(atrate:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/preroll(atrate:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/preroll%28atrate%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:3899f9747bd62843'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# preroll(atRate:completionHandler:)

<sub>Instance Method</sub>

Begins loading media data to prime the media pipelines for playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func preroll(atRate rate: Float, completionHandler: (@Sendable (Bool) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func preroll(atRate rate: Float) async -> Bool
```

## Parameters

- `rate` — The playback rate to use when determining how much data to load.

- `completionHandler` — A block to execute when the player finishes the load attempt. This block takes a single Boolean parameter that contains [true](../../swift/true.md) if the data was loaded or [false](../../swift/false.md) if there was a problem. For example, the value might be [false](../../swift/false.md) if the preroll was interrupted by a time change or incompatible rate change.

## Discussion

This method loads data starting at the item’s current playback time. The current rate for the playback item should always be 0 prior to calling this method. After the method calls the completion handler, you can change the item’s playback rate to begin playback.

If the player object is not ready to play (its [status](status-swift.property.md) property is not [AVPlayerStatusReadyToPlay](status-swift.enum/readytoplay.md)), this method throws an exception.

## See Also

### Synchronizing multiple players

- [- setRate:time:atHostTime:](<setrate(__time_athosttime_).md>) — Synchronizes the playback rate and time of the current item with an external source.
- [- cancelPendingPrerolls](<cancelpendingprerolls().md>) — Cancels any pending preroll requests and invokes the corresponding completion handlers, if present.
- [sourceClock](sourceclock.md) — A clock the player uses for item time bases.
- [masterClock](masterclock.md) — The host clock for item time bases. _(deprecated)_
