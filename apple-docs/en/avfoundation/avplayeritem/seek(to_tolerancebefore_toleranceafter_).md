---
title: 'seek(to:toleranceBefore:toleranceAfter:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（11.0 起废弃）, iPadOS 4.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.7+（10.13 起废弃）, tvOS 9.0+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avplayeritem/seek(to:tolerancebefore:toleranceafter:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/seek(to:tolerancebefore:toleranceafter:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/seek%28to%3Atolerancebefore%3Atoleranceafter%3A%29.json'
content_hash: 'sha256:ea9747e7ce3cd38d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# seek(to:toleranceBefore:toleranceAfter:)

<sub>Instance Method</sub>

Sets the current playback time within a specified time bound.

> [!warning] Deprecated
> Use [- seekToTime:toleranceBefore:toleranceAfter:completionHandler:](<seek(to_tolerancebefore_toleranceafter_completionhandler_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func seek(to time: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime)
```

## Parameters

- `time` — The time to which you would like to move the playback cursor.

- `toleranceBefore` — The tolerance allowed before `time`.

- `toleranceAfter` — The tolerance allowed after `time`.

## Discussion

The time seeked to will be within the range `[time-beforeTolerance, time+afterTolerance]`, and may differ from the specified time for efficiency. If you pass `kCMTimeZero` for both `toleranceBefore` and `toleranceAfter` (to request sample accurate seeking), you may incur additional decoding delay that impacts seeking performance.

Passing `kCMTimePositiveInfinity` for both `toleranceBefore` and `toleranceAfter` is the same as messaging [- seekToTime:](<seek(to_)-1dpto.md>) directly.

## See Also

### Related Documentation

- [- seekToTime:toleranceBefore:toleranceAfter:completionHandler:](<seek(to_tolerancebefore_toleranceafter_completionhandler_).md>) — Sets the current playback time within a specified time bound and invokes the specified block when the seek operation completes or is interrupted.
- [- seekToTime:completionHandler:](<seek(to_completionhandler_)-91gnw.md>) — Sets the current playback time to the specified time.

### Seeking through media

- [- seekToTime:](<seek(to_)-1dpto.md>) — Sets the current playback time to the specified time. _(deprecated)_
- [seek(to:)](<seek(to_)-5rt4x.md>) — Sets the current playback time to the time specified by the date object. _(deprecated)_
- [- seekToDate:](<seek(to_)-3s9d8.md>) — Sets the current playback time to the time specified by the date object. _(deprecated)_
