---
title: 'seek(to:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayer/seek(to:completionhandler:)-wr1l'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/seek(to:completionhandler:)-wr1l'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/seek%28to%3Acompletionhandler%3A%29-wr1l.json'
content_hash: 'sha256:7974978d074b4aed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# seek(to:completionHandler:)

<sub>Instance Method</sub>

Requests that the player seek to a specified date, and to notify you when the seek is complete.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func seek(to date: Date, completionHandler: @escaping @Sendable (Bool) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func seek(to date: Date) async -> Bool
```

## Parameters

- `date` — The time to which to seek.

- `completionHandler` — The block to invoke when the seek operation has either been completed or been interrupted. The block takes one argument: - **finished** — Indicates whether the seek operation completed.

## Discussion

Use this method to seek the current player item to the specified time and be notified when the operation completes. If the seek request completes without being interrupted (either by another seek request or by any other operation), the completion handler you provide is executed with the `finished` parameter set to [true](../../swift/true.md).

If another seek request is already in progress when you call this method, the completion handler for the in-progress seek request is executed immediately with the `finished` parameter set to [false](../../swift/false.md).

## See Also

### Seeking through media

- [- seekToTime:](<seek(to_)-87h2r.md>) — Requests that the player seek to a specified time.
- [- seekToTime:completionHandler:](<seek(to_completionhandler_)-75bls.md>) — Requests that the player seek to a specified time, and to notify you when the seek is complete.
- [- seekToTime:toleranceBefore:toleranceAfter:](<seek(to_tolerancebefore_toleranceafter_).md>) — Requests that the player seek to a specified time with the amount of accuracy specified by the time tolerance values.
- [- seekToTime:toleranceBefore:toleranceAfter:completionHandler:](<seek(to_tolerancebefore_toleranceafter_completionhandler_).md>) — Requests that the player seek to a specified time with the amount of accuracy specified by the time tolerance values, and to notify you when the seek is complete.
- [- seekToDate:](<seek(to_)-9h9qr.md>) — Requests that the player seek to a specified date.
