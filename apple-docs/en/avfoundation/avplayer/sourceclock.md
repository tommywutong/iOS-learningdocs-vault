---
title: sourceClock
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/sourceclock
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/sourceclock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/sourceclock.json'
content_hash: 'sha256:6c2a0d051fe5d37a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# sourceClock

<sub>Instance Property</sub>

A clock the player uses for item time bases.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var sourceClock: CMClock? { get set }
```

## Discussion

The default value is `nil`. Setting an explicit source clock is useful to synchronize video-only movies with audio that plays through a different audio device.

> [!important] Important
> Specifying a source clock for a device other than the one playing audio may cause audio to drift out of sync.

## See Also

### Synchronizing multiple players

- [- setRate:time:atHostTime:](<setrate(__time_athosttime_).md>) — Synchronizes the playback rate and time of the current item with an external source.
- [- prerollAtRate:completionHandler:](<preroll(atrate_completionhandler_).md>) — Begins loading media data to prime the media pipelines for playback.
- [- cancelPendingPrerolls](<cancelpendingprerolls().md>) — Cancels any pending preroll requests and invokes the corresponding completion handlers, if present.
- [masterClock](masterclock.md) — The host clock for item time bases. _(deprecated)_
