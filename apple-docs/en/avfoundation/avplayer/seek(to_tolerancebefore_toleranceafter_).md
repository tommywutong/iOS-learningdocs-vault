---
title: 'seek(to:toleranceBefore:toleranceAfter:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayer/seek(to:tolerancebefore:toleranceafter:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/seek(to:tolerancebefore:toleranceafter:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/seek%28to%3Atolerancebefore%3Atoleranceafter%3A%29.json'
content_hash: 'sha256:b740175eddb3fc08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# seek(to:toleranceBefore:toleranceAfter:)

<sub>Instance Method</sub>

Requests that the player seek to a specified time with the amount of accuracy specified by the time tolerance values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func seek(to time: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime)
```

## Parameters

- `time` — A time to seek to.

- `toleranceBefore` — A tolerance before the target time to allow.

- `toleranceAfter` — A tolerance after the target time to allow.

## Discussion

The player seeks within the range `[time-beforeTolerance, time+afterTolerance]`, and may differ from the specified time for efficiency. You can request sample accurate seeking by passing a time value of`kCMTimeZero` for both `toleranceBefore` and `toleranceAfter`. Sample accurate seeking may incur additional decoding delay which can impact seeking performance.

Passing `kCMTimePositiveInfinity` for both `toleranceBefore` and `toleranceAfter` is the same as messaging [- seekToTime:](<seek(to_)-87h2r.md>) directly.

## See Also

### Seeking through media

- [- seekToTime:](<seek(to_)-87h2r.md>) — Requests that the player seek to a specified time.
- [- seekToTime:completionHandler:](<seek(to_completionhandler_)-75bls.md>) — Requests that the player seek to a specified time, and to notify you when the seek is complete.
- [- seekToTime:toleranceBefore:toleranceAfter:completionHandler:](<seek(to_tolerancebefore_toleranceafter_completionhandler_).md>) — Requests that the player seek to a specified time with the amount of accuracy specified by the time tolerance values, and to notify you when the seek is complete.
- [- seekToDate:](<seek(to_)-9h9qr.md>) — Requests that the player seek to a specified date.
- [- seekToDate:completionHandler:](<seek(to_completionhandler_)-wr1l.md>) — Requests that the player seek to a specified date, and to notify you when the seek is complete.
