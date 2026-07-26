---
title: 'seek(to:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（11.0 起废弃）, iPadOS 4.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.7+（10.13 起废弃）, tvOS 9.0+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avplayeritem/seek(to:)-3s9d8'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/seek(to:)-3s9d8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/seek%28to%3A%29-3s9d8.json'
content_hash: 'sha256:d8fb570e5fd12bb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# seek(to:)

<sub>Instance Method</sub>

Sets the current playback time to the time specified by the date object.

> [!warning] Deprecated
> Use [- seekToDate:completionHandler:](<seek(to_completionhandler_)-1dibq.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
@MainActor func seek(to date: Date) -> Bool
```

## Parameters

- `date` — The time to which to seek.

## Return Value

[true](../../swift/true.md) if the playhead was moved to `date`, otherwise [false](../../swift/false.md).

## Discussion

For playback content that is associated with a range of dates, this method moves the playhead to point within that range. This method will fail (return [false](../../swift/false.md)) if `date` is outside the range or if the content is not associated with a range of dates.

## See Also

### Related Documentation

- [- seekToTime:toleranceBefore:toleranceAfter:completionHandler:](<seek(to_tolerancebefore_toleranceafter_completionhandler_).md>) — Sets the current playback time within a specified time bound and invokes the specified block when the seek operation completes or is interrupted.
- [- seekToTime:completionHandler:](<seek(to_completionhandler_)-91gnw.md>) — Sets the current playback time to the specified time.

### Seeking through media

- [- seekToTime:](<seek(to_)-1dpto.md>) — Sets the current playback time to the specified time. _(deprecated)_
- [- seekToTime:toleranceBefore:toleranceAfter:](<seek(to_tolerancebefore_toleranceafter_).md>) — Sets the current playback time within a specified time bound. _(deprecated)_
- [seek(to:)](<seek(to_)-5rt4x.md>) — Sets the current playback time to the time specified by the date object. _(deprecated)_
