---
title: 'seek(to:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritem/seek(to:completionhandler:)-1dibq'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/seek(to:completionhandler:)-1dibq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/seek%28to%3Acompletionhandler%3A%29-1dibq.json'
content_hash: 'sha256:b6aefe9514ccddb5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# seek(to:completionHandler:)

<sub>Instance Method</sub>

Sets the current playback time to the time specified by the date object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func seek(to date: Date, completionHandler: (@Sendable (Bool) -> Void)? = nil) -> Bool
```

## Parameters

- `date` — The time to which to seek.

- `completionHandler` — The block to invoke when the seek operation has either been completed or been interrupted. The block takes one argument: - **finished** — Indicates whether the seek operation completed.

## Return Value

[true](../../swift/true.md) if the playhead moved to the specified date or [false](../../swift/false.md) if it did not.

## Discussion

Use this method to seek to a specified time in the player item and be notified when the operation completes. If the seek request completes without being interrupted (either by another seek request or by any other operation), the completion handler you provide is executed with the `finished` parameter set to [true](../../swift/true.md).

If another seek request is already in progress when you call this method, the completion handler for the in-progress seek request is executed immediately with the `finished` parameter set to [false](../../swift/false.md).

## See Also

### Seeking through media

- [- seekToTime:completionHandler:](<seek(to_completionhandler_)-91gnw.md>) — Sets the current playback time to the specified time.
- [- seekToTime:toleranceBefore:toleranceAfter:completionHandler:](<seek(to_tolerancebefore_toleranceafter_completionhandler_).md>) — Sets the current playback time within a specified time bound and invokes the specified block when the seek operation completes or is interrupted.
- [- cancelPendingSeeks](<cancelpendingseeks().md>) — Cancels any pending seek requests and invokes the corresponding completion handlers if present.
