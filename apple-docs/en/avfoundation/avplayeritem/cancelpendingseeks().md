---
title: cancelPendingSeeks()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/cancelpendingseeks()
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/cancelpendingseeks()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/cancelpendingseeks%28%29.json'
content_hash: 'sha256:96e4b5f9c7505773'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# cancelPendingSeeks()

<sub>Instance Method</sub>

Cancels any pending seek requests and invokes the corresponding completion handlers if present.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func cancelPendingSeeks()
```

## Discussion

Use this method to cancel and release the completion handlers of pending seeks.

The `finished` parameter of the completion handlers will be set to [false](../../swift/false.md).

## See Also

### Seeking through media

- [- seekToTime:completionHandler:](<seek(to_completionhandler_)-91gnw.md>) — Sets the current playback time to the specified time.
- [- seekToTime:toleranceBefore:toleranceAfter:completionHandler:](<seek(to_tolerancebefore_toleranceafter_completionhandler_).md>) — Sets the current playback time within a specified time bound and invokes the specified block when the seek operation completes or is interrupted.
- [- seekToDate:completionHandler:](<seek(to_completionhandler_)-1dibq.md>) — Sets the current playback time to the time specified by the date object.
