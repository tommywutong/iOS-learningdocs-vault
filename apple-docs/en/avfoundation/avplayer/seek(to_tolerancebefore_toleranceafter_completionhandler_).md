---
title: 'seek(to:toleranceBefore:toleranceAfter:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayer/seek(to:tolerancebefore:toleranceafter:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/seek(to:tolerancebefore:toleranceafter:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/seek%28to%3Atolerancebefore%3Atoleranceafter%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:63ee8862fe455c80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# seek(to:toleranceBefore:toleranceAfter:completionHandler:)

<sub>Instance Method</sub>

Requests that the player seek to a specified time with the amount of accuracy specified by the time tolerance values, and to notify you when the seek is complete.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func seek(to time: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime, completionHandler: @escaping @Sendable (Bool) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func seek(to time: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime) async -> Bool
```

## Parameters

- `time` — The time to which to seek.

- `toleranceBefore` — The tolerance allowed before `time`.

- `toleranceAfter` — The tolerance allowed after `time`.

- `completionHandler` — The block to invoke when the seek operation has either been completed or been interrupted. The block takes one argument: - **finished** — Indicated whether the seek operation completed.

## Discussion

Use this method to seek to a specified time for the current player item and to be notified when the seek operation is complete.

The time seeked to will be within the range `[time-beforeTolerance, time+afterTolerance]`, and may differ from the specified time for efficiency. You can request sample accurate seeking by passing a time value of`kCMTimeZero` for both `toleranceBefore` and `toleranceAfter`. Sample accurate seeking may incur additional decoding delay which can impact seeking performance.

Invoking this method with `toleranceBefore` set to [positiveInfinity](../../coremedia/cmtime/positiveinfinity.md) and `toleranceAfter` set to [positiveInfinity](../../coremedia/cmtime/positiveinfinity.md) is the same as invoking [- seekToTime:](<seek(to_)-87h2r.md>).

The completion handler for any prior seek request that is still in process will be invoked immediately with the `finished` parameter set to [false](../../swift/false.md). If the new request completes without being interrupted by another seek request or by any other operation the specified completion handler will be invoked with the `finished` parameter set to [true](../../swift/true.md).

## See Also

### Seeking through media

- [- seekToTime:](<seek(to_)-87h2r.md>) — Requests that the player seek to a specified time.
- [- seekToTime:completionHandler:](<seek(to_completionhandler_)-75bls.md>) — Requests that the player seek to a specified time, and to notify you when the seek is complete.
- [- seekToTime:toleranceBefore:toleranceAfter:](<seek(to_tolerancebefore_toleranceafter_).md>) — Requests that the player seek to a specified time with the amount of accuracy specified by the time tolerance values.
- [- seekToDate:](<seek(to_)-9h9qr.md>) — Requests that the player seek to a specified date.
- [- seekToDate:completionHandler:](<seek(to_completionhandler_)-wr1l.md>) — Requests that the player seek to a specified date, and to notify you when the seek is complete.
