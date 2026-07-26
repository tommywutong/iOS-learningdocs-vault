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
doc_path: '/documentation/avfoundation/avplayeritem/seek(to:)-1dpto'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/seek(to:)-1dpto'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/seek%28to%3A%29-1dpto.json'
content_hash: 'sha256:cbb6a5d69e157fa8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# seek(to:)

<sub>Instance Method</sub>

Sets the current playback time to the specified time.

> [!warning] Deprecated
> Use [- seekToTime:completionHandler:](<seek(to_completionhandler_)-91gnw.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
@MainActor func seek(to time: CMTime)
```

## Parameters

- `time` — The time to which to seek.

## Discussion

The time seeked to may differ from the specified time for efficiency. For sample accurate seeking see [- seekToTime:toleranceBefore:toleranceAfter:](<seek(to_tolerancebefore_toleranceafter_).md>).

## See Also

### Related Documentation

- [- seekToTime:toleranceBefore:toleranceAfter:completionHandler:](<seek(to_tolerancebefore_toleranceafter_completionhandler_).md>) — Sets the current playback time within a specified time bound and invokes the specified block when the seek operation completes or is interrupted.
- [- seekToTime:completionHandler:](<seek(to_completionhandler_)-91gnw.md>) — Sets the current playback time to the specified time.

### Seeking through media

- [- seekToTime:toleranceBefore:toleranceAfter:](<seek(to_tolerancebefore_toleranceafter_).md>) — Sets the current playback time within a specified time bound. _(deprecated)_
- [seek(to:)](<seek(to_)-5rt4x.md>) — Sets the current playback time to the time specified by the date object. _(deprecated)_
- [- seekToDate:](<seek(to_)-3s9d8.md>) — Sets the current playback time to the time specified by the date object. _(deprecated)_
