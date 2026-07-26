---
title: rate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferrendersynchronizer/rate
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/rate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrendersynchronizer/rate.json'
content_hash: 'sha256:1aff6a2ec25acd9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferRenderSynchronizer](../avsamplebufferrendersynchronizer.md)

# rate

<sub>Instance Property</sub>

The current playback rate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var rate: Float { get set }
```

## Discussion

A value of `0.0` means playback has stopped. A value of `1.0` tells the renderer to play at the natural rate of the media. This property must be greater than or equal to `0.0`.

## See Also

### Accessing time information

- [- currentTime](<currenttime().md>) — Returns the current time of the synchronizer.
- [timebase](timebase.md) — The synchronizer’s rendering timebase which determines how it interprets timestamps.
- [- setRate:time:](<setrate(__time_).md>) — Sets the renderer’s time and rate.
- [- setRate:time:atHostTime:](<setrate(__time_athosttime_).md>) — Sets the playback rate and the relationship between the current time and host time.
- [AVSampleBufferRenderSynchronizerRateDidChangeNotification](ratedidchangenotification.md) — The synchronizer’s rendering rate changed.
- [delaysRateChangeUntilHasSufficientMediaData](delaysratechangeuntilhassufficientmediadata.md) — A Boolean value that Indicates whether the playback should start immediately on rate change requests.
