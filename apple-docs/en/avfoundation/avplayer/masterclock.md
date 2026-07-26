---
title: masterClock
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+（18.0 起废弃）, iPadOS 6.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.8+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）, watchOS 1.0+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avplayer/masterclock
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/masterclock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/masterclock.json'
content_hash: 'sha256:a97b416b79fae707'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# masterClock

<sub>Instance Property</sub>

The host clock for item time bases.

> [!warning] Deprecated
> Use [sourceClock](sourceclock.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
nonisolated var masterClock: CMClock? { get set }
```

## Discussion

The default value of this property is `NULL`, which means that the host clock is the automatic choice. When non-`NULL`, this property overrides the automatic choice of host clock for item time bases. This is most useful when you’re synchronizing video-only movies with audio from another source.

> [!important] Important
> If you specify a host clock other than the appropriate audio device’s clock, the audio may drift out of sync.

## See Also

### Synchronizing multiple players

- [- setRate:time:atHostTime:](<setrate(__time_athosttime_).md>) — Synchronizes the playback rate and time of the current item with an external source.
- [- prerollAtRate:completionHandler:](<preroll(atrate_completionhandler_).md>) — Begins loading media data to prime the media pipelines for playback.
- [- cancelPendingPrerolls](<cancelpendingprerolls().md>) — Cancels any pending preroll requests and invokes the corresponding completion handlers, if present.
- [sourceClock](sourceclock.md) — A clock the player uses for item time bases.
