---
title: 'seek(to:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayer/seek(to:)-9h9qr'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/seek(to:)-9h9qr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/seek%28to%3A%29-9h9qr.json'
content_hash: 'sha256:37748155d2a2b235'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# seek(to:)

<sub>Instance Method</sub>

Requests that the player seek to a specified date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func seek(to date: Date)
```

## Parameters

- `date` — The time to which to seek.

## Discussion

The time to which the player seeks may differ from the specified `date` for efficiency. For sample accurate seeking see [- seekToTime:toleranceBefore:toleranceAfter:](<seek(to_tolerancebefore_toleranceafter_).md>).

## See Also

### Seeking through media

- [- seekToTime:](<seek(to_)-87h2r.md>) — Requests that the player seek to a specified time.
- [- seekToTime:completionHandler:](<seek(to_completionhandler_)-75bls.md>) — Requests that the player seek to a specified time, and to notify you when the seek is complete.
- [- seekToTime:toleranceBefore:toleranceAfter:](<seek(to_tolerancebefore_toleranceafter_).md>) — Requests that the player seek to a specified time with the amount of accuracy specified by the time tolerance values.
- [- seekToTime:toleranceBefore:toleranceAfter:completionHandler:](<seek(to_tolerancebefore_toleranceafter_completionhandler_).md>) — Requests that the player seek to a specified time with the amount of accuracy specified by the time tolerance values, and to notify you when the seek is complete.
- [- seekToDate:completionHandler:](<seek(to_completionhandler_)-wr1l.md>) — Requests that the player seek to a specified date, and to notify you when the seek is complete.
