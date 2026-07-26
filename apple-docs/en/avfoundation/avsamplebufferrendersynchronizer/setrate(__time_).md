---
title: 'setRate(_:time:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avsamplebufferrendersynchronizer/setrate(_:time:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/setrate(_:time:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrendersynchronizer/setrate%28_%3Atime%3A%29.json'
content_hash: 'sha256:20c1b9319b5e66ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferRenderSynchronizer](../avsamplebufferrendersynchronizer.md)

# setRate(_:time:)

<sub>Instance Method</sub>

Sets the renderer’s time and rate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setRate(_ rate: Float, time: CMTime)
```

## Parameters

- `rate` — The new timebase rate. This value must be greater than or equal to `0.0`.

- `time` — The new timebase time. This value must be greater than or equal to [zero](../../coremedia/cmtime/zero.md), or [invalid](../../coremedia/cmtime/invalid.md).

## Discussion

This method first sets the new time and then the new rendering rate. A `rate` value of `0.0` means that playback has stopped while a `rate` value of `1.0` indicates playback should be at the natural rate of the media.

## See Also

### Accessing time information

- [- currentTime](<currenttime().md>) — Returns the current time of the synchronizer.
- [timebase](timebase.md) — The synchronizer’s rendering timebase which determines how it interprets timestamps.
- [rate](rate.md) — The current playback rate.
- [- setRate:time:atHostTime:](<setrate(__time_athosttime_).md>) — Sets the playback rate and the relationship between the current time and host time.
- [AVSampleBufferRenderSynchronizerRateDidChangeNotification](ratedidchangenotification.md) — The synchronizer’s rendering rate changed.
- [delaysRateChangeUntilHasSufficientMediaData](delaysratechangeuntilhassufficientmediadata.md) — A Boolean value that Indicates whether the playback should start immediately on rate change requests.
