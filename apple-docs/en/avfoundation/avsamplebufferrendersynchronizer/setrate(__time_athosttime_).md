---
title: 'setRate(_:time:atHostTime:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, macOS 11.3+, tvOS 14.5+, visionOS 1.0+, watchOS 7.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avsamplebufferrendersynchronizer/setrate(_:time:athosttime:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/setrate(_:time:athosttime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrendersynchronizer/setrate%28_%3Atime%3Aathosttime%3A%29.json'
content_hash: 'sha256:9061df3855760b99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferRenderSynchronizer](../avsamplebufferrendersynchronizer.md)

# setRate(_:time:atHostTime:)

<sub>Instance Method</sub>

Sets the playback rate and the relationship between the current time and host time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setRate(_ rate: Float, time: CMTime, atHostTime hostTime: CMTime)
```

## Parameters

- `rate` — A new timebase rate. This value must be greater than or equal to `0.0`.

- `time` — A new timebase time. This value must be greater than or equal to [zero](../../coremedia/cmtime/zero.md), or [invalid](../../coremedia/cmtime/invalid.md).

- `hostTime` — A new host time. This value must be greater than or equal to [zero](../../coremedia/cmtime/zero.md), or [invalid](../../coremedia/cmtime/invalid.md).

## See Also

### Accessing time information

- [- currentTime](<currenttime().md>) — Returns the current time of the synchronizer.
- [timebase](timebase.md) — The synchronizer’s rendering timebase which determines how it interprets timestamps.
- [rate](rate.md) — The current playback rate.
- [- setRate:time:](<setrate(__time_).md>) — Sets the renderer’s time and rate.
- [AVSampleBufferRenderSynchronizerRateDidChangeNotification](ratedidchangenotification.md) — The synchronizer’s rendering rate changed.
- [delaysRateChangeUntilHasSufficientMediaData](delaysratechangeuntilhassufficientmediadata.md) — A Boolean value that Indicates whether the playback should start immediately on rate change requests.
