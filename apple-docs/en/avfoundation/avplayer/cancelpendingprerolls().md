---
title: cancelPendingPrerolls()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/cancelpendingprerolls()
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/cancelpendingprerolls()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/cancelpendingprerolls%28%29.json'
content_hash: 'sha256:b78bb1a1dd0342bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# cancelPendingPrerolls()

<sub>Instance Method</sub>

Cancels any pending preroll requests and invokes the corresponding completion handlers, if present.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func cancelPendingPrerolls()
```

## Discussion

This method cancels and releases the completion handlers for any pending prerolls. The finished parameter of the completion handlers passed to [- prerollAtRate:completionHandler:](<preroll(atrate_completionhandler_).md>) will be set to `false`.

## See Also

### Synchronizing multiple players

- [- setRate:time:atHostTime:](<setrate(__time_athosttime_).md>) — Synchronizes the playback rate and time of the current item with an external source.
- [- prerollAtRate:completionHandler:](<preroll(atrate_completionhandler_).md>) — Begins loading media data to prime the media pipelines for playback.
- [sourceClock](sourceclock.md) — A clock the player uses for item time bases.
- [masterClock](masterclock.md) — The host clock for item time bases. _(deprecated)_
