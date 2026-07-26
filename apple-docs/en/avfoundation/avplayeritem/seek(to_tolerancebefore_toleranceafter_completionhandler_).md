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
doc_path: '/documentation/avfoundation/avplayeritem/seek(to:tolerancebefore:toleranceafter:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/seek(to:tolerancebefore:toleranceafter:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/seek%28to%3Atolerancebefore%3Atoleranceafter%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:efa4230c97a64ab6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# seek(to:toleranceBefore:toleranceAfter:completionHandler:)

<sub>Instance Method</sub>

Sets the current playback time within a specified time bound and invokes the specified block when the seek operation completes or is interrupted.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func seek(to time: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime, completionHandler: (@Sendable (Bool) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func seek(to time: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime) async -> Bool
```

## Parameters

- `time` — The time to which to seek.

- `toleranceBefore` — The temporal tolerance before `time`. Pass [zero](../../coremedia/cmtime/zero.md) to request sample accurate seeking (this may incur additional decoding delay).

- `toleranceAfter` — The temporal tolerance after `time`. Pass [zero](../../coremedia/cmtime/zero.md) to request sample accurate seeking (this may incur additional decoding delay).

- `completionHandler` — The block to invoke when the seek operation has finished.

## Discussion

Use this method to seek to a specified time for the item.

The time seeked to will be within the range `[time-toleranceBefore, time+toleranceAfter]` and may differ from `time` for efficiency.

Invoking this method with [positiveInfinity](../../coremedia/cmtime/positiveinfinity.md) for `toleranceBefore` and `toleranceAfter` is the same as invoking [- seekToTime:completionHandler:](<seek(to_completionhandler_)-91gnw.md>) directly.

Seeking is constrained by the collection of seekable time ranges. If you seek to a time outside all of the seekable ranges, the seek will result in a current time within the seekable ranges.

## See Also

### Seeking through media

- [- seekToTime:completionHandler:](<seek(to_completionhandler_)-91gnw.md>) — Sets the current playback time to the specified time.
- [- seekToDate:completionHandler:](<seek(to_completionhandler_)-1dibq.md>) — Sets the current playback time to the time specified by the date object.
- [- cancelPendingSeeks](<cancelpendingseeks().md>) — Cancels any pending seek requests and invokes the corresponding completion handlers if present.
